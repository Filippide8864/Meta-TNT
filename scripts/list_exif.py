import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

def list_exif(file_path):
    try:
        print(f"Listing EXIF metadata of: {file_path}")
        result = subprocess.run(['exiftool', '-EXIF', file_path], capture_output=True, text=True, check=True)
        print(f"EXIF metadata of {file_path}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error listing EXIF metadata of {file_path}: {e}")

def process_directory(directory):
    files = []
    for root, _, file_list in os.walk(directory):
        for file in file_list:
            files.append(os.path.join(root, file))

    with ThreadPoolExecutor() as executor:
        executor.map(list_exif, files)

def main(directory):
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        sys.exit(1)

    process_directory(directory)

if __name__ == "__main__":
    main(sys.argv[1])
