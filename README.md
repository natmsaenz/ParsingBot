*******ParsingBot*******
This project was created for Bosch México Audio triage team. With different modules in it, this script will help us to:
-Decompress files into an specific path
-Create new paths so we can decompress files into them
-Convert .dlt files into .txt files so we can handle them more easily
-Compress all the .txt files into one for our convenience
-Detect incidences from an input
All this in a single script and while moving the files to an specific directory.

*******Requirements to use the script*******
-Having the DLTViewer app installed.
-Having the latest version of Python installed.
-Knowing the basics of using the Windows Command Prompt.

*******How to use the script*******
-Once we have the DLTViewer app installed, it's important to change the dltviewerpath (line 44 of the script), on the DLTtoTXT module using the path where the app was installed.
-Open the Windows Command prompt and write the command for python, the name of the script, the path of the file to decompress and its arguments (the names of the folders where the final decompressed files will be stored), like the next example:
 *py LogAndConcatenation.py TargetPath arguments(paths ID1, ID2....)*
 

