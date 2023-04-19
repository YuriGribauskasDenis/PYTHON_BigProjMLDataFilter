from pathlib import Path

def get_folder_adr(file):
    return Path(file).resolve().parent

def get_file_adr(file):
    return Path(file).resolve()