import argparse
import os
import sys
from scripts import remove_metadata, list_metadata, add_metadata
from scripts import remove_exif, list_exif, add_exif
from scripts import remove_xmp, list_xmp, add_xmp
from scripts import remove_ipptc, list_ipptc, add_ipptc

def main():
    parser = argparse.ArgumentParser(description="Meta-TNT - Gestione dei Metadati dei File")

    subparsers = parser.add_subparsers(dest="command", help="Comandi disponibili")

    # Comandi generali
    remove_parser = subparsers.add_parser("remove", help="Rimuove tutti i metadati dai file in una directory specificata")
    remove_parser.add_argument("directory", help="Directory dei file")

    list_parser = subparsers.add_parser("list", help="Elenca tutti i metadati dei file in una directory specificata")
    list_parser.add_argument("directory", help="Directory dei file")

    add_parser = subparsers.add_parser("add", help="Aggiunge metadati specifici ai file in una directory specificata")
    add_parser.add_argument("directory", help="Directory dei file")
    add_parser.add_argument("metadata", nargs='+', help="Metadati da aggiungere")

    # Comandi EXIF
    remove_exif_parser = subparsers.add_parser("remove_exif", help="Rimuove i metadati EXIF dai file in una directory specificata")
    remove_exif_parser.add_argument("directory", help="Directory dei file")

    list_exif_parser = subparsers.add_parser("list_exif", help="Elenca i metadati EXIF dei file in una directory specificata")
    list_exif_parser.add_argument("directory", help="Directory dei file")

    add_exif_parser = subparsers.add_parser("add_exif", help="Aggiunge metadati EXIF specifici ai file in una directory specificata")
    add_exif_parser.add_argument("directory", help="Directory dei file")
    add_exif_parser.add_argument("metadata", nargs='+', help="Metadati EXIF da aggiungere")

    # Comandi XMP
    remove_xmp_parser = subparsers.add_parser("remove_xmp", help="Rimuove i metadati XMP dai file in una directory specificata")
    remove_xmp_parser.add_argument("directory", help="Directory dei file")

    list_xmp_parser = subparsers.add_parser("list_xmp", help="Elenca i metadati XMP dei file in una directory specificata")
    list_xmp_parser.add_argument("directory", help="Directory dei file")

    add_xmp_parser = subparsers.add_parser("add_xmp", help="Aggiunge metadati XMP specifici ai file in una directory specificata")
    add_xmp_parser.add_argument("directory", help="Directory dei file")
    add_xmp_parser.add_argument("metadata", nargs='+', help="Metadati XMP da aggiungere")

    # Comandi IPTC
    remove_ipptc_parser = subparsers.add_parser("remove_ipptc", help="Rimuove i metadati IPTC dai file in una directory specificata")
    remove_ipptc_parser.add_argument("directory", help="Directory dei file")

    list_ipptc_parser = subparsers.add_parser("list_ipptc", help="Elenca i metadati IPTC dei file in una directory specificata")
    list_ipptc_parser.add_argument("directory", help="Directory dei file")

    add_ipptc_parser = subparsers.add_parser("add_ipptc", help="Aggiunge metadati IPTC specifici ai file in una directory specificata")
    add_ipptc_parser.add_argument("directory", help="Directory dei file")
    add_ipptc_parser.add_argument("metadata", nargs='+', help="Metadati IPTC da aggiungere")

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
        print(f"Errore durante l'esecuzione del comando: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()