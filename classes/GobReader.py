import os

from classes.GobFile import GobFile
from constants import offsets
from utils.gen_path import gen_path


class GobReader():
    """This class reads a .gob container, processes its contents, and outputs individual files as file_list"""

    def __init__(self, filename: str) -> None:
        self.cur_offset = 0
        self.filename = filename
        with open(filename, 'rb') as f:
            self.data = f.read()
        self.file_list = []
        self.n_files = 0

    def process(self) -> None:
        """Runs the gob processing pipeline"""
        self._process_header_()
        self._process_file_entries_()
        self._process_file_contents_()
    
    def write_files(self, root_directory: str) -> None:
        """
        Writes file contents in file_list to disk.

        :param root_directory: the directory to be used as a root for relative 
                               paths in the .gob file.
        """
        if root_directory[-1] != '\\':
            root_directory = root_directory + '\\'
        for file in self.file_list:
            file_path = root_directory + file.file_path
            try:
                os.makedirs('\\'.join(file_path.split('\\')[:-1]))
            except FileExistsError:
                pass
            with open(file_path, 'wb') as f:
                f.write(file.file_data)
        print(f'Saved {self.filename} to {root_directory[:-1]}')

    def _read_bytes_(self, n_bytes: int) -> bytes:
        """Reads n_bytes bytes and moves the cursor the same amount"""
        out = self.data[self.cur_offset:self.cur_offset+n_bytes]
        self.cur_offset += n_bytes
        return out
    
    def _process_header_(self) -> None:
        """Reads the header and parses how many files are in this .gob file from it."""
        self.header = self._read_bytes_(offsets.HEADER_SIZE)
        self.n_files = int.from_bytes(self.header[offsets.HEADER_FILECOUNT_OFFSET:], byteorder='little')
    
    def _process_file_entries_(self) -> None:
        """Processes the amount of file entries mapped by header metadata. Assumes the cursor is at the end of the header."""
        for i in range(self.n_files):
            entry = self._read_file_entry_()
            self.file_list.append(entry)

    def _read_file_entry_(self) -> GobFile:
        """Reads each individual file entry and parses its fields. Returns a GobFile object."""
        entry_bytes = self._read_bytes_(offsets.TREE_ENTRY_SIZE)
        first_value = int.from_bytes(entry_bytes[offsets.TREE_UNK_DATA_OFFSET:offsets.TREE_UNK_DATA_OFFSET+4], byteorder='little')
        file_size = int.from_bytes(entry_bytes[offsets.TREE_SIZE_OFFSET:offsets.TREE_SIZE_OFFSET+4], byteorder='little')
        file_path = ''
        for i in entry_bytes[offsets.TREE_STR_OFFSET:]:
            if i == 0:
                break
            file_path += chr(i)
        return GobFile(
            first_value,
            file_size,
            file_path,
        )
    
    def _process_file_contents_(self):
        """Processes file contents for each file in file_list. Assumes the cursor is at the end of the file tree block."""
        for i in self.file_list:
            i.file_data = self._read_bytes_(i.file_size)
