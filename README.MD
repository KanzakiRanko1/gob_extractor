# Gob Extractor

## About the Project
This software is purpose built for unpacking .gob files from LucasArts's 1997 title Star Wars Jedi Knight: Dark Forces II for preservation purposes.

It works by reading the metadata in the .gob file and splitting it in separate files, in similar fashion to what the game does in memory. With some further exploration, repacking .gob files for mods might be possible. Other games by Lucas Arts, be them in the same series or not, might also use this file format, and be compatible off the bat.

The main goal of this project was to be able to be able to repack the Brazilian Portuguese localization of the game, released in CD form in 1997 by Brasoft, into the Steam and GOG.com releases, but other uses might come down the road.

## Requirements
Python 3.6 or newer. That's it. It uses no third-party dependencies. This project was developed under and tested with Python 3.10.10.

## Usage
There are two supported usage modes through the -f flag and the -g flag.

### File mode:
```bash
Usage:
python gob_extractor.py -f <FILE_PATH>
```
This extracts the file `FILE_PATH` points to, creates a folder called `extracted_files` in your current directory, a subfolder for your .gob file and unpacks it there.

### Batch mode:
```bash
Usage:
python gob_extractor.py -g
```
This reads your current directory recursively, creates a folder called `extracted_files` in your current directory, a subfolder for each .gob file found and unpacks them there.

Recommended usage for Batch mode would be opening your terminal in the game folder and running `python <FULL_PATH_TO_GOB_EXTRACTOR> -g`. Copying the .gob files to your Gob Extractor folder will also work but might lead to making a messy directory.

## License