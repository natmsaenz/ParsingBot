import os
from os import system
import sys
import shutil
from os import walk
from io import open
import glob

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
    if len(list_of_arguments) >= folderIDsStart+1:
        if os.path.exists(targetPath):
            # Reserve all necessary directories.
            for i in range(2, len(list_of_arguments)):
                newDir = os.path.join(targetPath, sys.argv[i])
                os.mkdir(newDir)
                dirDict.update({sys.argv[i]: newDir})
                print(newDir + " created!")
            # Sort files at path into target directories
            for (dirPath, dirNames, fileNames) in walk(os.path.join(targetPath, ".")):
                for name in fileNames:
                    for key, path in dirDict.items():
                        if name.find(key) != -1:
                            shutil.move(os.path.join(dirPath, name), path) #debug
                            os.system("cls")
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
   if(len(sys.argv) > 2 ):
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
#testing the changes, not working yet
#The code it´s not working with this changes
def goThroughTxt(dirname, output_filename):
    read_files = glob.glob("*.txt")
    with open(output_filename, 'w') as outfile: #we open the new txt file to write on it
        for filename in read_files:
            if filename.endswith('.txt'):
                 with open(os.path.join(dirname, filename), errors='ignore') as infile:
                    print("Working on it...")
                    os.system("cls")
                    outfile.write(infile.read())
                    shutil.move('finalTxt.txt', targetPath)  
#-----------------------------------------------------------------------------------------------------------------
#Use to find the insidence from an input
def insidence():
    # Open the txt file
    with open('finalTxt.txt', 'r') as f: 
        content = f.readlines()
    #Substring to search for.
    insidence = input('Enter the word to search: ')
    # create a list for the coincidences
    coincidences = []
    for line in content:
        if insidence in line:
            coincidences.append(line)
    # we open the new txt file and write on it with all the insidence
    with open('insidence.txt', 'w') as f:
        for coincidence in coincidences:
            f.write(coincidence)
    shutil.move('insidence.txt', targetPath)
    shutil.move('finalTxt.txt', targetPath) 
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
folderIDsStart = 2
dirDict = {}

if len(list_of_arguments) >= folderIDsStart+1:

    if os.path.isdir(file_name_to_parse):
        decompress(file_name_to_parse)
        DLTtoTXT()
        goThroughTxt(file_name_to_parse, 'finalTxt.txt')
        insidence()
        dir_new()
        print("Everything done") 
    else:
        decompress(new_dir_path)
else:
    print("Not enough arguments provided, expected: LogAndConcatenation.py <path_to_traverse> <ID1> <ID2> (...)")