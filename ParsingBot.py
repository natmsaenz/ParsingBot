import sys
from os import path

from scripts import convert_DLT_to_TXT, create_new_folders, sort_files, decompress_files_from_path, find_incidence

if __name__ == "__main__":
    args = sys.argv
    args_len = len(args)
    target_path = args[1]
    script_path = path.dirname(__file__)
    new_dir_path = path.join(script_path, path.splitext(target_path)[0])

    if args_len >= 0:
        if path.isdir(target_path):
            decompress_files_from_path(target_path)
            
            if (args_len >= 1):
                convert_DLT_to_TXT(target_path)
            else:
                print("Number of passed arguments is:",
                      len(sys.argv), " expecting: 2")
    
            find_incidence(target_path)
            create_new_folders(target_path)
            sort_files(target_path)

            print("Everything done")
        else:
            decompress_files_from_path(new_dir_path)
    else:
        print("Unexpected Error")
