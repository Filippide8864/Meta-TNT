# Meta-TNT

Meta-TNT è un tool per gestire i metadati dei file.

## Installazione

1. Clona il repository:
   ```sh
   git clone https://github.com/tuo_utente/Meta-TNT.git
   cd Meta-TNT
   ```

2. Installa `exiftool`:
   - Su Ubuntu/Debian:
     ```sh
     sudo apt-get update
     sudo apt-get install exiftool
     ```
   - Su macOS:
     ```sh
     brew install exiftool
     ```
   - Su Windows:
     Scarica `exiftool` dal sito ufficiale e aggiungilo al tuo PATH.

3. Verifica l'installazione di `exiftool`:
   ```sh
   exiftool -ver
   ```

## Uso

Esegui il comando `python main.py -h` per visualizzare l'aiuto e i comandi disponibili.

### Esempi di Comandi

#### Rimuovere Tutti i Metadati
```sh
python main.py remove /percorso/alla/tua/directory
```

#### Elencare Tutti i Metadati
```sh
python main.py list /percorso/alla/tua/directory
```

#### Aggiungere Metadati Specifici
```sh
python main.py add /percorso/alla/tua/directory -Author="Nome Autore" -Copyright="Anno Copyright"
```

#### Rimuovere Metadati EXIF
```sh
python main.py remove_exif /percorso/alla/tua/directory
```

#### Elencare Metadati EXIF
```sh
python main.py list_exif /percorso/alla/tua/directory
```

#### Aggiungere Metadati EXIF Specifici
```sh
python main.py add_exif /percorso/alla/tua/directory -EXIF:Make="Marca" -EXIF:Model="Modello"
```

#### Rimuovere Metadati XMP
```sh
python main.py remove_xmp /percorso/alla/tua/directory
```

#### Elencare Metadati XMP
```sh
python main.py list_xmp /percorso/alla/tua/directory
```

#### Aggiungere Metadati XMP Specifici
```sh
python main.py add_xmp /percorso/alla/tua/directory -XMP:CreatorTool="Strumento Creatore"
```

#### Rimuovere Metadati IPTC
```sh
python main.py remove_ipptc /percorso/alla/tua/directory
```

#### Elencare Metadati IPTC
```sh
python main.py list_ipptc /percorso/alla/tua/directory
```

#### Aggiungere Metadati IPTC Specifici
```sh
python main.py add_ipptc /percorso/alla/tua/directory -IPTC:By-line="Nome Autore"
```

## Note Aggiuntive

- **Backup**: Prima di eseguire operazioni che modificano i metadati, considera di fare backup dei file originali.
- **Compatibilità**: `exiftool` supporta una vasta gamma di formati di file, ma non tutti i metadati possono essere gestiti da tutti i formati. Consulta la documentazione di `exiftool` per ulteriori dettagli.