import os
from os import system
import sys
import shutil
from os import walk
from io import open

#Use to extract all the compress files
def decompress(dir_path):
    content = os.listdir(dir_path)
    #extract de GZ files
    for name in content:
        if os.path.splitext(name)[1] in compressed_extension:
            system(f"7z e -y -o{dir_path} {os.path.join(dir_path,name)}") #Debug
            os.system("cls")
            #os.remove(os.path.join(dir_path,name)) only if it´s necessary to eliminate the compress directory
#------------------------------------------------------------------------------------------------------------------------
#Use to make the new paths and put the descompress files with the ID arguments into the new paths
def dir_new():
    foldersToCreate = ['CriticalSoc','Soc', 'Vip', "ISVS","PATACHMI"]
    if len(foldersToCreate) >= folderIDsStart+1:
        if os.path.exists(targetPath):
            # Reserve all necessary directories.
            for i in range(len(foldersToCreate)):
                newDir = os.path.join(targetPath, foldersToCreate[i])
                os.mkdir(newDir)
                dirDict.update({foldersToCreate[i]: newDir})
                print(newDir + " created!")
            # Sort files at path into target directories
            for (dirPath, dirNames, fileNames) in walk(os.path.join(targetPath, ".")):
                for name in fileNames:
                    for key, path in dirDict.items():
                        if name.find(key) != -1:
                            shutil.move(os.path.join(dirPath, name), os.path.join(path, name))
                            #shutil.copytree(os.path.join(dirPath, name), path,dirs_exist_ok=True) #debug
                            #os.remove(os.path.join(dirPath, name))
                            break
        else:
            print("ERROR: no valid filesystem path entered!")
    else:
        print("Not enough arguments provided, expected: LogAndConcatenation.py <path_to_traverse> <ID1> <ID2> (...)")
#----------------------------------------------------------------------------------------------------------------------------
#Use to convert from .dlt file to .txt file
def DLTtoTXT():
   dltLabel = ".dlt"
   dltViewerPath = "C:\Program Files (x86)\dltviewer\DltViewerSDK\dlt_viewer.exe"
   if(len(sys.argv) > 1 ):
        # we assign the target path  to the path put it before
        targetPath = sys.argv[1]
        #Compare if the target path and de DLTpath exist
        if(os.path.exists(targetPath) and os.path.exists(dltViewerPath)):
            print("Valid target path detected, text iteration starts!")
            for (dirPath, dirNames, fileNames) in walk(os.path.join(targetPath, ".")):
                for name in fileNames:
                    targetFile = os.path.join(dirPath,name)
                    #If the file is .dlt
                    if dltLabel in targetFile:
                        #With the dltviewer app convert from .dlt to .txt
                        os.system("\"" + dltViewerPath + "\"" + " -c "  + targetFile + " " + targetFile + ".txt")
                    else:
                        print("No .DLT detected")
        else:
            print("Invalid target path provided!")
   else:
        print("Number of passed arguments is:", len(sys.argv), " expecting: 2")
#------------------------------------------------------------------------------------------------------------------------------
#go through .txt files and save them into another txt file
def goThroughTxt(dir_path):
    keyword = input('Enter the word to search: ')
    # output name
    output_file = 'insidence.txt'
    # we set the outfile on write mode
    with open(output_file, 'w') as out:
        for filename in os.listdir(dir_path):
            if filename.endswith('.txt'):
                # we open all the .txt files on read mode
                with open(os.path.join(dir_path, filename), 'r', errors="ignore") as f:
                    lines = f.readlines()
                    matches = 0
                    # we write the coincidences on the outfile 
                    for line in lines: 
                        if keyword in line:
                            out.write(f'{line}')
                            matches += 1 
                    out.write(f'{matches} matches found on: {filename}\n')                     
    shutil.copy2('insidence.txt', targetPath)
    os.remove("insidence.txt")
####################################################################
#                                                                  #
#                           SCRIPT                                 # 
#                                                                  #
####################################################################

list_of_arguments = sys.argv
file_name_to_parse = list_of_arguments[1]
script_path = os.path.dirname(__file__)
new_dir_path = os.path.join(script_path,os.path.splitext(file_name_to_parse)[0])
compressed_extension = '.tar', '.rar', '.zip', '.7z', '.gz' 
targetPath = sys.argv[1]
help_PathIndex = 1
folderIDsStart = 0
dirDict = {}
#------------------------------------------------------------------------------------------
if len(list_of_arguments) >= folderIDsStart:
    if os.path.isdir(file_name_to_parse):
        decompress(file_name_to_parse)
        DLTtoTXT()
        goThroughTxt(file_name_to_parse)
        dir_new()
        print("Everything done") 
    else:
        decompress(new_dir_path)
else:
    print("Unexpected Error")