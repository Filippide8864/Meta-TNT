import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

def remove_exif(file_path):
    try:
        print(f"Rimozione dei metadati EXIF da: {file_path}")
        subprocess.run(['exiftool', '-all=', '-tagsfromfile', '@', '-all:all', file_path], check=True)
        print(f"Metadati EXIF rimossi da: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante la rimozione dei metadati EXIF da {file_path}: {e}")

def process_directory(directory):
    files = []
    for root, _, file_list in os.walk(directory):
        for file in file_list:
            files.append(os.path.join(root, file))

    with ThreadPoolExecutor() as executor:
        executor.map(remove_exif, files)

def main(directory):
    if not os.path.isdir(directory):
        print(f"La directory {directory} non esiste.")
        sys.exit(1)

    process_directory(directory)

if __name__ == "__main__":
    main(sys.argv[1])
