# Hot_Linker
Creates HTML that maps Kraken Metagenomics Excel output to NCBI Dashboard, checks hotlist of organisms

This py script takes the excel file that reuslts from a kraken metagenomics anlysis.

1) Run the sript.
2) use the file browser to choose an ecel file of organisms
3) use the file browser to choose an excel file of organisms to cross check if in the Kreaken file
4) Click on the Link button to run the script.
5) The scriot will impor the files, crosscheck for common organisms, then generates an HTML with links to NCBI

Requires import:

1) Pandas
2) PySimpleGUI
3) time
4) csv, os
5) webbrowser

Ancillary required files:

1) Image files for LED
2) Hot-list of organisms to cross check if in Kraken file.
