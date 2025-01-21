import argparse
import os
import sys
from scripts import remove_metadata, list_metadata, add_metadata
from scripts import remove_exif, list_exif, add_exif
from scripts import remove_xmp, list_xmp, add_xmp
from scripts import remove_ipptc, list_ipptc, add_ipptc

def main():
    parser = argparse.ArgumentParser(description="Meta-TNT - File Metadata Management")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # General commands
    remove_parser = subparsers.add_parser("remove", help="Remove all metadata from files in a specified directory")
    remove_parser.add_argument("directory", help="Directory of files")

    list_parser = subparsers.add_parser("list", help="List all metadata of files in a specified directory")
    list_parser.add_argument("directory", help="Directory of files")

    add_parser = subparsers.add_parser("add", help="Add specific metadata to files in a specified directory")
    add_parser.add_argument("directory", help="Directory of files")
    add_parser.add_argument("metadata", nargs='+', help="Metadata to add")

    # EXIF commands
    remove_exif_parser = subparsers.add_parser("remove_exif", help="Remove EXIF metadata from files in a specified directory")
    remove_exif_parser.add_argument("directory", help="Directory of files")

    list_exif_parser = subparsers.add_parser("list_exif", help="List EXIF metadata of files in a specified directory")
    list_exif_parser.add_argument("directory", help="Directory of files")

    add_exif_parser = subparsers.add_parser("add_exif", help="Add specific EXIF metadata to files in a specified directory")
    add_exif_parser.add_argument("directory", help="Directory of files")
    add_exif_parser.add_argument("metadata", nargs='+', help="EXIF metadata to add")

    # XMP commands
    remove_xmp_parser = subparsers.add_parser("remove_xmp", help="Remove XMP metadata from files in a specified directory")
    remove_xmp_parser.add_argument("directory", help="Directory of files")

    list_xmp_parser = subparsers.add_parser("list_xmp", help="List XMP metadata of files in a specified directory")
    list_xmp_parser.add_argument("directory", help="Directory of files")

    add_xmp_parser = subparsers.add_parser("add_xmp", help="Add specific XMP metadata to files in a specified directory")
    add_xmp_parser.add_argument("directory", help="Directory of files")
    add_xmp_parser.add_argument("metadata", nargs='+', help="XMP metadata to add")

    # IPTC commands
    remove_ipptc_parser = subparsers.add_parser("remove_ipptc", help="Remove IPTC metadata from files in a specified directory")
    remove_ipptc_parser.add_argument("directory", help="Directory of files")

    list_ipptc_parser = subparsers.add_parser("list_ipptc", help="List IPTC metadata of files in a specified directory")
    list_ipptc_parser.add_argument("directory", help="Directory of files")

    add_ipptc_parser = subparsers.add_parser("add_ipptc", help="Add specific IPTC metadata to files in a specified directory")
    add_ipptc_parser.add_argument("directory", help="Directory of files")
    add_ipptc_parser.add_argument("metadata", nargs='+', help="IPTC metadata to add")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "remove":
            remove_metadata.main(args.directory)
        elif args.command == "list":
            list_metadata.main(args.directory)
        elif args.command == "add":
            add_metadata.main(args.directory, args.metadata)
        elif args.command == "remove_exif":
            remove_exif.main(args.directory)
        elif args.command == "list_exif":
            list_exif.main(args.directory)
        elif args.command == "add_exif":
            add_exif.main(args.directory, args.metadata)
        elif args.command == "remove_xmp":
            remove_xmp.main(args.directory)
        elif args.command == "list_xmp":
            list_xmp.main(args.directory)
        elif args.command == "add_xmp":
            add_xmp.main(args.directory, args.metadata)
        elif args.command == "remove_ipptc":
            remove_ipptc.main(args.directory)
        elif args.command == "list_ipptc":
            list_ipptc.main(args.directory)
        elif args.command == "add_ipptc":
            add_ipptc.main(args.directory, args.metadata)
    except Exception as e:
        print(f"Error executing command: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()