import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

def add_exif(file_path, metadata):
    try:
        print(f"Adding EXIF metadata to: {file_path}")
        subprocess.run(['exiftool', '-overwrite_original'] + metadata + [file_path], check=True)
        print(f"EXIF metadata added to: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error adding EXIF metadata to {file_path}: {e}")

def process_directory(directory, metadata):
    files = []
    for root, _, file_list in os.walk(directory):
        for file in file_list:
            files.append(os.path.join(root, file))

    with ThreadPoolExecutor() as executor:
        executor.map(lambda file: add_exif(file, metadata), files)

def main(directory, metadata):
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        sys.exit(1)

    process_directory(directory, metadata)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
