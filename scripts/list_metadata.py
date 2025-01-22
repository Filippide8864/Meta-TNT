import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor
from PyPDF2 import PdfReader
from zipfile import ZipFile

def list_pdf_metadata(file_path):
    try:
        print(f"Listing metadata of PDF file: {file_path}")
        reader = PdfReader(file_path)
        metadata = reader.metadata
        print(f"Metadata of PDF file {file_path}:\n{metadata}")
    except Exception as e:
        print(f"Error listing metadata of PDF file {file_path}: {e}")

def list_odt_metadata(file_path):
    try:
        print(f"Listing metadata of ODT file: {file_path}")
        with ZipFile(file_path, 'r') as odt_file:
            odt_file.extractall('temp_odt')

        meta_file_path = 'temp_odt/meta.xml'
        if os.path.exists(meta_file_path):
            with open(meta_file_path, 'r') as meta_file:
                metadata = meta_file.read()
                print(f"Metadata of ODT file {file_path}:\n{metadata}")
        else:
            print(f"No metadata found in ODT file {file_path}")
    except Exception as e:
        print(f"Error listing metadata of ODT file {file_path}: {e}")

def list_metadata(file_path):
    try:
        if file_path.lower().endswith(('.m4a', '.mp3', '.wav', '.flac')):
            print(f"Listing metadata of audio file: {file_path}")
            result = subprocess.run(['ffmpeg', '-i', file_path], capture_output=True, text=True, check=True)
            print(f"Metadata of audio file {file_path}:\n{result.stderr}")
        elif file_path.lower().endswith(('.zip', '.ds_store')):
            print(f"Skipping unsupported file: {file_path}")
        elif file_path.lower().endswith('.pdf'):
            list_pdf_metadata(file_path)
        elif file_path.lower().endswith('.odt'):
            list_odt_metadata(file_path)
        else:
            print(f"Listing metadata of: {file_path}")
            result = subprocess.run(['exiftool', file_path], capture_output=True, text=True, check=True)
            print(f"Metadata of {file_path}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error listing metadata of {file_path}: {e}")

def process_directory(directory):
    files = []
    for root, _, file_list in os.walk(directory):
        for file in file_list:
            files.append(os.path.join(root, file))

    with ThreadPoolExecutor() as executor:
        executor.map(list_metadata, files)

def main(directory):
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        sys.exit(1)

    process_directory(directory)

if __name__ == "__main__":
    main(sys.argv[1])