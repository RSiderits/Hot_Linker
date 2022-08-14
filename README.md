# Hot_Linker

Creates an HTML that formats the organisms from a Kraken Metagenomics Excel output file, as an NCBI search, to the organism's NCBI Dashboard, 
then checks a hotlist of organisms against the main file.

This py script takes the excel file that reuslts from a kraken metagenomics anlysis.  

Do this: 

1) Insert "Thiomargarita magnifica" into the kraken file to serve as a control for the cross reference to the hot-list.
2) Change the name of the organism colum to "organism"

Instructions:

1) run the sript.
2) use the file browser to choose an ecel file of organisms
3) use the file browser to choose an excel file of organisms to cross check if in the Kreaken file
4) Click on the "Link" button to run the script.
5) The script will import the excel files, crosscheck for common organisms, 
   then it creates an HTML with links to NCBI
6) Runs a control to make sure the cross reference is working: "Thiomargarita magnifica"
7) The script waits 2 seconds and then opens the HTML doc (titled: zzz.html) in the default browser.
8) Sorts organism list on "Reads"

Requires import:

1) Pandas
2) PySimpleGUI
3) time
4) csv, os
5) webbrowser

Ancillary required files, in same folder:

1) Image files for LED
2) Hot-list of organisms to cross check if in Kraken file.
