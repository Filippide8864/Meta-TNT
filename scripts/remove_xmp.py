import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

def remove_xmp(file_path):
    try:
        print(f"Removing XMP metadata from: {file_path}")
        subprocess.run(['exiftool', '-XMP=', file_path], check=True)
        print(f"XMP metadata removed from: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error removing XMP metadata from {file_path}: {e}")

def process_directory(directory):
    files = []
    for root, _, file_list in os.walk(directory):
        for file in file_list:
            files.append(os.path.join(root, file))

    with ThreadPoolExecutor() as executor:
        executor.map(remove_xmp, files)

def main(directory):
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        sys.exit(1)

    process_directory(directory)

if __name__ == "__main__":
    main(sys.argv[1])
