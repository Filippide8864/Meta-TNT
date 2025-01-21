import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

def list_exif(file_path):
    try:
        print(f"Elenco dei metadati EXIF di: {file_path}")
        result = subprocess.run(['exiftool', '-EXIF', file_path], capture_output=True, text=True, check=True)
        print(f"Metadati EXIF di {file_path}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'elenco dei metadati EXIF di {file_path}: {e}")

def process_directory(directory):
    files = []
    for root, _, file_list in os.walk(directory):
        for file in file_list:
            files.append(os.path.join(root, file))

    with ThreadPoolExecutor() as executor:
        executor.map(list_exif, files)

def main(directory):
    if not os.path.isdir(directory):
        print(f"La directory {directory} non esiste.")
        sys.exit(1)

    process_directory(directory)

if __name__ == "__main__":
    main(sys.argv[1])
