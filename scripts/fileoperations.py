from shutil import copy2, move
from os import path, listdir, mkdir, remove, system, walk
from .setup import load_settings


def sort_files(target_path: str):
    # Sort files at path into target directories
    for (file_path, directories, file_names) in walk(target_path):
        for name in file_names:
            for dir in directories:
                if name.find(dir) != -1:
                    move(path.join(file_path, name),
                            path.join(file_path, dir))
                    break


def create_new_folders(target_path: str):
    directories = {}

    FOLDERS_TO_CREATE = load_settings("FOLDERS_TO_CREATE")

    if len(FOLDERS_TO_CREATE) >= 1:
        if path.exists(target_path):
            # Reserve all necessary directories.
            for folder in FOLDERS_TO_CREATE:
                folder_exists = path.exists(path.join(target_path, folder))
                new_dir = path.join(target_path, folder)
                directories.update({folder: new_dir})
                if not folder_exists:
                    mkdir(new_dir)
                print(f"{new_dir} created!")
        else:
            print("ERROR: no valid filesystem path entered!")
    else:
        print("Not enough arguments provided, expected: ParsingBot.py <path_to_traverse>")


def convert_DLT_to_TXT(target_path: str, from_extension: str = ".dlt", to_extension: str = ".txt"):
    DLT_VIEWER_PATH = load_settings("DLT_VIEWER_PATH")

    if(path.exists(target_path) and path.exists(DLT_VIEWER_PATH)):
        print("Valid target path detected, text iteration starts!")
        for (dirPath, _, fileNames) in walk(target_path):
            for name in fileNames:
                target_file = path.join(dirPath, name)
                # If the file is .dlt

                if target_file.endswith(from_extension):
                     # With the dltviewer app convert from .dlt to .txt
                    system(
                        f'"{DLT_VIEWER_PATH}" -c {target_file} {target_file}{to_extension}')
    else:
        print("Invalid target path provided!")


def find_incidence(target_path: str, output_file: str = "incidence.txt"):
    keyword = load_settings("INCIDENCE_KEYWORD") if load_settings(
        "INCIDENCE_KEYWORD") else input('Enter the word to search: ')

    with open(output_file, 'w') as out:
        ext = [".log", ".txt"]
        for filename in listdir(target_path):
            if filename.endswith(tuple(ext)):
                # we open all the .txt files on read mode
                with open(path.join(target_path, filename), 'r', errors="ignore") as f:
                    lines = f.readlines()
                    matches = 0
                    # we write the coincidences on the outfile
                    for line in lines:
                        if keyword in line:
                            out.write(f'{line}')
                            matches += 1
                    out.write(f'{matches} matches found on: {filename}\n')

    copy2(output_file, target_path)
    remove(output_file)
