# Disk Analyzer

A Python tool to find out what's taking up space on your computer.

> 🚧 Work in progress. I'm building this project step by step as I get back into programming.

## Features

- [x] List the largest files in a folder
- [x] Show the total size of each folder
- [x] Skip files and folders that can't be accessed
- [ ] Find duplicate files
- [ ] Safe cleanup (files go to the Recycle Bin, never deleted permanently)
- [ ] Graphical interface

## Requirements

- Python 3.14 or newer

## How to use

Clone the repository:

```bash
git clone git@github.com:BrandonErick/disk-analyzer.git
cd disk-analyzer
```

Scan your Downloads folder (default):

```bash
python scanner.py
```

Scan any folder you choose:

```bash
python scanner.py ~
python scanner.py "C:/Users/YourName/Documents"
```

It shows the 10 largest folders and the 10 largest files inside that folder.

> **Note:** some folders, like OneDrive or files synced from your phone, may show files that are stored in the cloud or on another device, so they don't actually take up space on your disk. Always check before deleting anything.

## Contributing

Ideas and contributions are welcome. Feel free to open an issue or a pull request.

## License

This project is open source under the [MIT License](LICENSE).
