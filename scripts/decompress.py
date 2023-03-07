from os import path, name, listdir, system

COMPRESSED_FILE_EXTENSIONS = '.tar', '.rar', '.zip', '.7z', '.gz'


def cls():
    system('cls' if name == 'nt' else 'clear')


def decompress_files_from_path(target_path: str):
    list_file = listdir(target_path)
    for file_name in list_file:
        file_extension = path.splitext(file_name)[1]
        if file_extension in COMPRESSED_FILE_EXTENSIONS:
            system(
                f"7z e -y -o{target_path} {path.join(target_path,file_name)}")
            cls()
