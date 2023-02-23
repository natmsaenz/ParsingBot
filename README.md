#ParsingBot
This project was created for Bosch México Audio triage team. With different modules in it, this script will help us to:
-Decompress files into an specific path
-Create new paths so we can decompress files into them
-Convert .dlt files into .txt files so we can handle them more easily
-Compress all the .txt files into one for our convenience
-Detect incidences from an input
All this in a single script and while moving the files to an specific directory.

##Requirements to use the script
-Having the DLTViewer app installed, the script works with the 2.17.0 stable version. For the script to work, the DLTViewer has to be located on this path: C:\Program Files (x86)\dltviewer\DltViewerSDK\dlt_viewer.exe
*If you don´t have the DLTviewer app, you can download from this package:* https://inside-docupedia.bosch.com/confluence/display/gen3generic/DLT-viewer
-Before using the script, you have to extract the files of the folder you downloaded, for example:
[ screenshot for the extraction example ](C:\Users\MNA2GA\Documents\ParsingBot\exampleScreenshot_1.jpg)
__
-Having the latest version of Python installed*.
-Having the 7z software installed
-Knowing the basics of using the Windows Command Prompt.
-*as far as we know, the script works well with the 3.9.2 version of Python*

##How to use the script

-Open the Windows Command prompt and write the command for python, the name of the script, the path of the file to decompress and its arguments (the names of the folders where the final decompressed files will be stored), like the next example:
 `py LogAndConcatenation.py TargetPath`
- **You should always put _py_ before running any python script, after that, you put the name of the script _LogAndConcatenation.py_ . Always make sure your script is on the correct location when you use it, for example:**

[Example screenshot](C:\Users\MNA2GA\Documents\ParsingBot\consoleScreenshot.jpg)
_In this case, the script is located in the C:\Users\MNA2GA folder, so we'll run it that way_

- **And finally, add the _TargetPath_ which is the path of the folder you want to decompress with the script**
 
 

