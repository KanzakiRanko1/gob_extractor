import argparse
import glob
import sys

from classes.GobReader import GobReader
from utils import gen_path

description = """
Extracts .gob files from the LucasArts title Star Wars Jedi Knight: Dark Forces II (and possibly others that share an engine), maintaining directory structures.
For using the -g flag, please run this script from another directory or add your game folder as a subfolder of this script.
"""

parser = argparse.ArgumentParser('gob_extractor', description=description)
# parser.add_argument('-h', '--help', help='Print this help text.')
parser.add_argument('-g', '--glob', action='store_true', help='Extract all .gob files in children directories from current working directory.')
parser.add_argument('-f', '--file', help='Relative path to the .gob file you want to extract.', type=str)
args = parser.parse_args()

if __name__ == '__main__':
    if args.glob:
        file_list = glob.glob('**/*.gob', recursive=True)
        print(f'Running for {len(file_list)} gob files...')
        for gob_path in file_list:
            br = GobReader(gob_path)
            br.process()
            br.write_files(gen_path.gen_path('extracted_files', gob_path))
        sys.exit(0)
    if args.file:
        gob_path = args.file
        br = GobReader(gob_path)
        br.process()
        br.write_files(gen_path.gen_path('extracted_files', gob_path))
        sys.exit(0)
    parser.print_help()
    sys.exit(1)