# Meta-TNT

Meta-TNT is a versatile tool designed to manage and manipulate file metadata. Whether you need to remove, list, or add metadata to various file types, Meta-TNT has you covered. From images and documents to audio and video files, Meta-TNT simplifies the process of handling metadata, ensuring your files are organized and secure.

## Introduction

Metadata is essential information embedded within files that describes the file's content, origin, and other details. Managing metadata is crucial for privacy, security, and organizational purposes. Meta-TNT simplifies this process by providing a user-friendly interface to handle metadata for a wide range of file formats.

## Why Use Meta-TNT?

- **Privacy**: Remove sensitive metadata from your files to protect your personal information.
- **Security**: Ensure your files are secure by removing or modifying metadata that could be exploited.
- **Organization**: Keep your files organized by adding or modifying metadata to categorize and search for files easily.
- **Compatibility**: Supports a wide range of file formats, making it a versatile tool for various needs.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Filippide8864/Meta-TNT
   cd Meta-TNT
   ```

2. **Install `exiftool`**:
   - On Ubuntu/Debian:
     ```sh
     sudo apt-get update
     sudo apt-get install exiftool
     ```
   - On macOS:
     ```sh
     brew install exiftool
     ```
   - On Windows:
     Download `exiftool` from the official site and add it to your PATH.

3. **Install `ffmpeg`**:
   - On Ubuntu/Debian:
     ```sh
     sudo apt-get update
     sudo apt-get install ffmpeg
     ```
   - On macOS:
     ```sh
     brew install ffmpeg
     ```
   - On Windows:
     Download `ffmpeg` from the official site and add it to your PATH.

4. **Verify the Installation**:
   ```sh
   exiftool -ver
   ffmpeg -version
   ```

5. **Install Python Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run `python main.py -h` to display help and available commands.

### Command Examples

#### Remove All Metadata
```sh
python main.py remove /path/to/your/directory
```
This command will remove all metadata from files in the specified directory.

#### List All Metadata
```sh
python main.py list /path/to/your/directory
```
This command will list all metadata from files in the specified directory.

#### Add Specific Metadata
```sh
python main.py add /path/to/your/directory -Author="Author Name" -Copyright="Copyright Year"
```
This command will add specific metadata to files in the specified directory.

#### Remove EXIF Metadata
```sh
python main.py remove_exif /path/to/your/directory
```
This command will remove EXIF metadata from files in the specified directory.

#### List EXIF Metadata
```sh
python main.py list_exif /path/to/your/directory
```
This command will list EXIF metadata from files in the specified directory.

#### Add Specific EXIF Metadata
```sh
python main.py add_exif /path/to/your/directory -EXIF:Make="Brand" -EXIF:Model="Model"
```
This command will add specific EXIF metadata to files in the specified directory.

#### Remove XMP Metadata
```sh
python main.py remove_xmp /path/to/your/directory
```
This command will remove XMP metadata from files in the specified directory.

#### List XMP Metadata
```sh
python main.py list_xmp /path/to/your/directory
```
This command will list XMP metadata from files in the specified directory.

#### Add Specific XMP Metadata
```sh
python main.py add_xmp /path/to/your/directory -XMP:CreatorTool="Creator Tool"
```
This command will add specific XMP metadata to files in the specified directory.

#### Remove IPTC Metadata
```sh
python main.py remove_ipptc /path/to/your/directory
```
This command will remove IPTC metadata from files in the specified directory.

#### List IPTC Metadata
```sh
python main.py list_ipptc /path/to/your/directory
```
This command will list IPTC metadata from files in the specified directory.

#### Add Specific IPTC Metadata
```sh
python main.py add_ipptc /path/to/your/directory -IPTC:By-line="Author Name"
```
This command will add specific IPTC metadata to files in the specified directory.

## Additional Notes

- **Backup**: Before performing operations that modify metadata, consider backing up the original files.
- **Compatibility**: `exiftool` supports a wide range of file formats, but not all metadata can be managed by all formats.

## Unsupported File Extensions

Meta-TNT currently does not support the following file extensions:

- `.zip`
- `.ds_store`

These files will be skipped during metadata operations.

## Conclusion

Meta-TNT is a powerful tool for managing file metadata. Whether you're a photographer, videographer, or just someone who wants to keep their files organized, Meta-TNT can help you manage metadata with ease. Give it a try and see how it can simplify your workflow!

If you have any questions or need further assistance, feel free to reach out. Happy organizing!
