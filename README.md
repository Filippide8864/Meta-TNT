# Meta-TNT

Meta-TNT is a tool for managing the metadata of files.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Filippide8864/Meta-TNT.git
   cd Meta-TNT
   ```

2. Installa `exiftool`:
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

3. Verify the installation of `exiftool`:
   ```sh
   exiftool -ver
   ```

4. Installa le dipendenze Python:
   ```sh
   pip install -r requirements.txt
   ```

## Use

Run the command `python main.py -h` to view the help and available commands.

### Examples of Commands

#### Remove All Metadata
``sh
python main.py remove /path/to/your/ directory
```

#### List All Metadata
``sh
python main.py list /path/to/your/ directory
```

#### Add Specific Metadata
``sh
python main.py add /path/to/your/ directory -Author=‘Author Name’ -Copyright="Copyright Year’
```

#### Remove EXIF Metadata
``sh
python main.py remove_exif /path/to/your/directory
```

#### List EXIF Metadata
``sh
python main.py list_exif /path/to/your/ directory
```

#### Add Specific EXIF Metadata
``sh
python main.py add_exif /path/to/your/directory -EXIF:Make=‘Make’ -EXIF:Model="Model’
```

#### Remove XMP Metadata
``sh
python main.py remove_xmp /path/to/your/ directory
```

#### List XMP Metadata
``sh
python main.py list_xmp /path/to/your/ directory
```

#### Add specific XMP Metadata
``sh
python main.py add_xmp /path/to/your/ directory -XMP:CreatorTool="Creator Tool’
```

#### Remove IPTC Metadata
``sh
python main.py remove_ipptc /path/to/your/ directory
```

#### List IPTC Metadata
``sh
python main.py list_ipptc /path/to/your/ directory
```

#### Add Specific IPTC Metadata
``sh
python main.py add_ipptc /path/to/your/ directory -IPTC:By-line="Author Name’
```

Translated with www.DeepL.com/Translator (free version)

## Additional Notes
-**Backup**: Before performing operations that modify metadata, consider backing up the original files.
-**Compatibility**: `exiftool` supports a wide range of file formats, but not all metadata can be handled by all formats. See the `exiftool` documentation for more details.