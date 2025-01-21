import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

def remove_metadata(file_path):
    try:
        print(f"Removing metadata from: {file_path}")
        subprocess.run(['exiftool', '-all=', file_path], check=True)
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
