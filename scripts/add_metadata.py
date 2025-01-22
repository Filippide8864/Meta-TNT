import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor
from PyPDF2 import PdfReader, PdfWriter
from zipfile import ZipFile

def add_pdf_metadata(file_path, metadata):
    try:
        print(f"Adding metadata to PDF file: {file_path}")
        reader = PdfReader(file_path)
        writer = PdfWriter()

        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        for key, value in metadata.items():
            writer.add_metadata({key: value})

        with open(file_path, 'wb') as output_file:
            writer.write(output_file)

        print(f"Metadata added to PDF file: {file_path}")
    except Exception as e:
        print(f"Error adding metadata to PDF file {file_path}: {e}")

def add_odt_metadata(file_path, metadata):
    try:
        print(f"Adding metadata to ODT file: {file_path}")
        with ZipFile(file_path, 'r') as odt_file:
            odt_file.extractall('temp_odt')

        meta_file_path = 'temp_odt/meta.xml'
        if os.path.exists(meta_file_path):
            with open(meta_file_path, 'w') as meta_file:
                meta_file.write('<meta>\n')
                for key, value in metadata.items():
                    meta_file.write(f'<{key}>{value}</{key}>\n')
                meta_file.write('</meta>')

        with ZipFile(file_path, 'w') as odt_file:
            for root, _, files in os.walk('temp_odt'):
                for file in files:
                    odt_file.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), 'temp_odt'))

        print(f"Metadata added to ODT file: {file_path}")
    except Exception as e:
        print(f"Error adding metadata to ODT file {file_path}: {e}")

def add_metadata(file_path, metadata):
    try:
        if file_path.lower().endswith(('.m4a', '.mp3', '.wav', '.flac')):
            print(f"Adding metadata to audio file: {file_path}")
            tmp_file = f'{file_path}.tmp.m4a'
            subprocess.run(['ffmpeg', '-i', file_path, '-map_metadata', '-1', '-codec', 'copy', '-f', 'ipod', tmp_file], check=True)
            os.replace(tmp_file, file_path)
            print(f"Metadata added to audio file: {file_path}")
        elif file_path.lower().endswith(('.zip', '.ds_store')):
            print(f"Skipping unsupported file: {file_path}")
        elif file_path.lower().endswith('.pdf'):
            add_pdf_metadata(file_path, metadata)
        elif file_path.lower().endswith('.odt'):
            add_odt_metadata(file_path, metadata)
        else:
            print(f"Adding metadata to: {file_path}")
            subprocess.run(['exiftool', '-overwrite_original'] + metadata + [file_path], check=True)
            print(f"Metadata added to: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error adding metadata to {file_path}: {e}")

def process_directory(directory, metadata):
    files = []
    for root, _, file_list in os.walk(directory):
        for file in file_list:
            files.append(os.path.join(root, file))

    with ThreadPoolExecutor() as executor:
        executor.map(lambda file: add_metadata(file, metadata), files)

def main(directory, metadata):
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        sys.exit(1)

    process_directory(directory, metadata)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])