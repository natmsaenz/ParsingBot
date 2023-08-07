# ParsingBot


This project was created for Bosch México Audio Americas team. With different modules in it, it will help us to:

-Decompress files into an specific path.

-Convert .dlt files into .txt files so we can handle them more easily.

-Create new folders to sort the decompressed files into them, each corresponding to the file and folder name.

-Find the incidences of a keyword and save them in a text file.

## Requirements to use the script

- Having the DLTViewer app installed, the script works with the 2.17.0 stable version.

-*If you don´t have the DLTviewer app, you can download from this package:*  <https://inside-docupedia.bosch.com/confluence/display/gen3generic/DLT-viewer>

- Having the 7z software installed to decompress files.

- Before using the script, you have to extract the files of the folder you downloaded, for example:
![example image for compressed folder](Miscellaneous%20images/example_1.jpg)
![example image for extracting files](Miscellaneous%20images/example_2.jpg)

- Having the latest version of Python installed. This project works well with versions starting from 3.9.2.

- Knowing the basics of using the Windows Command Prompt and handling text files.

## How to use the script

- Open the settings.txt file, there, you will find all the settings for the script to work properly such as the folder names(Soc, Vip, etc.), the incidence word to search, time at which it is executed and the path of the DLTViewer. All of these can be modified according to the necessities of anybody that's using the script, in case that any of the fields are empty, you should not worry, the program has default values established so it can still work.
-*Notes:*

-*For the DLT_VIEWER_PATH: add the path where the app is located IN YOUR COMPUTER*

-*Add the folder names with the following format: ["name of your folder example"] and a comma between each of them, if there's more than one*

-*Keep the quotation marks where they are when modifying any of the fields*

-*When modifying the INCIDENCE_KEYWORD field, add a comma between each word, if there's more than one. When searching an incidence word from the console, add the words with just a space between them*

- Open the Windows Command prompt and write the command for python, the name of the script, the path of the file to decompress and its arguments (the names of the folders where the final decompressed files will be stored), like the next example:
  `py ParsingBot.py TargetPath`

- You should always put the command `py` before running any python script, after that, you put the name of the script: `ParsingBot.py`. Always make sure your script is on the correct location when you use it, for example:

![console example image](Miscellaneous%20images/example_3.jpg)
-*In this case, the script is located in the C:\Users\MNA2GA\Documents\ParsingBot folder, so we'll run it that way*

- Finally, add the `TargetPath`, which is the path of the folder you want to decompress with the script

 And that's it! now you just have to wait for the script to do its job and you'll have all the files decompressed and converted in their specified locations, and an incidence file with all the keywords to search.😊
