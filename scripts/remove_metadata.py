import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor
from PyPDF2 import PdfReader, PdfWriter
from zipfile import ZipFile

def remove_pdf_metadata(file_path):
    try:
        print(f"Removing metadata from PDF file: {file_path}")
        reader = PdfReader(file_path)
        writer = PdfWriter()

        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        with open(file_path, 'wb') as output_file:
            writer.write(output_file)

        print(f"Metadata removed from PDF file: {file_path}")
    except Exception as e:
        print(f"Error removing metadata from PDF file {file_path}: {e}")

def remove_odt_metadata(file_path):
    try:
        print(f"Removing metadata from ODT file: {file_path}")
        with ZipFile(file_path, 'r') as odt_file:
            odt_file.extractall('temp_odt')

        meta_file_path = 'temp_odt/meta.xml'
        if os.path.exists(meta_file_path):
            os.remove(meta_file_path)

        with ZipFile(file_path, 'w') as odt_file:
            for root, _, files in os.walk('temp_odt'):
                for file in files:
                    odt_file.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), 'temp_odt'))

        print(f"Metadata removed from ODT file: {file_path}")
    except Exception as e:
        print(f"Error removing metadata from ODT file {file_path}: {e}")

def remove_metadata(file_path):
    try:
        if file_path.lower().endswith(('.m4a', '.mp3', '.wav', '.flac')):
            print(f"Removing metadata from audio file: {file_path}")
            tmp_file = f'{file_path}.tmp.m4a'
            subprocess.run(['ffmpeg', '-i', file_path, '-map_metadata', '-1', '-codec', 'copy', '-f', 'ipod', tmp_file], check=True)
            os.replace(tmp_file, file_path)
            print(f"Metadata removed from audio file: {file_path}")
        elif file_path.lower().endswith(('.zip', '.ds_store')):
            print(f"Skipping unsupported file: {file_path}")
        elif file_path.lower().endswith('.pdf'):
            remove_pdf_metadata(file_path)
        elif file_path.lower().endswith('.odt'):
            remove_odt_metadata(file_path)
        else:
            print(f"Removing metadata from: {file_path}")
            subprocess.run(['exiftool', '-all=', '-overwrite_original', file_path], check=True)
            print(f"Metadata removed from: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error removing metadata from {file_path}: {e}")

def process_directory(directory):
    files = []
    for root, _, file_list in os.walk(directory):
        for file in file_list:
            files.append(os.path.join(root, file))

    with ThreadPoolExecutor() as executor:
        executor.map(remove_metadata, files)

def main(directory):
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        sys.exit(1)

    process_directory(directory)

if __name__ == "__main__":
    main(sys.argv[1])