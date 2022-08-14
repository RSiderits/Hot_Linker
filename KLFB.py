# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:09:07 2022

@author: R. siderits MD

Platform: RZR

Loc: Parabiotics Research Node: 1

Notes:

1) includes "Thiomargarita magnifica" as CONTROL for Datframe intersect
2) change names of columns to "organism"
3) Sorts on "reads"
4) Each new Hotlist can be versioned or simply kept current    


"""


# import modules -------------------------------------------------------------

import pandas as pd
import time
import PySimpleGUI as sg
import csv, os
import webbrowser

# Functions ------------------------------------------------------------------


#TODO: create a GUI file browser ---------------------------------------------

working_directory = os.getcwd()

sg.theme('LightGrey3')

layout=[
        
 # Handle layout of GUI
  
             
 # Kraken file import:
            
        [sg.InputText("Kraken", key="-FILE_PATH-", font=("calibri",15), size=(70, 1),\
                      enable_events=True), 
         
        sg.FileBrowse(initial_folder=working_directory,\
                      file_types=[("Excel files", "*.xlsx")])],
       
 # Hotlist:
        
        [sg.InputText("Hot_LIST", key="-FILE_PATH2-", font=("calibri",15), size=(70, 1),\
                     enable_events=True), 
         
        sg.FileBrowse(initial_folder=working_directory,\
                     file_types=[("Excel files", "*.xlsx")])],
            
            
 # Buttons to link and Exit:
            
        [sg.Button("Link", enable_events=True, pad=20, size=(4,1),\
                   font=("calibri",20), key="K_link"), 
         
         sg.Button("Exit", size=(4,1), font=("calibri",20))],
       
            
 # LED    
            
        [sg.Image("grey1.png", key="K_glow", pad=20, size=(50,50)),
        
        
         sg.MLine("Hotlist Crosscheck", key="HLC",\
                    enable_events=True, size=(35,3), pad=20, font=("calibri",20))]
       
        ]           
  

# Handle a world of "GUI-IFs"


window=sg.Window("Shotgun Search Linker", layout)


while True:    # Handle events
     
    event, values = window.read()
    
        
    if event == sg.WIN_CLOSED or event == "Exit":
        
        break
    
 # ----------------------------------------
        
    
    window["K_glow"].Update("grey1.png")
    time.sleep(1)
    window["K_glow"].Update("red1.png")
         
    if event == "K_link":
       
         window["K_glow"].Update("red1.png")
         
          
         excel_file=values["-FILE_PATH-"]
         
         excel_file2=values["-FILE_PATH2-"]
         
         data1=pd.read_excel(excel_file, sheet_name=\
                             "1000up_Kraken2-species_only.xls", usecols=[1,5])
         
                  
         data2=pd.read_excel(excel_file2, sheet_name="Organism_list")
                
         
         data4=pd.merge(data1, data2, how='inner')
         print()
         print("Organisms in hotlist and Kraken search:")
         print(data4)
         print()
         
         
         window["HLC"].Update(data4.loc[:,"organism"])
         
         window["K_glow"].Update("green1.png")
               
         sg.Popup('HTML written', button_type=5, grab_anywhere=True,\
                  auto_close=2)
         
         time.sleep(2)
         
         break    

           

# Set up parts of HTML search string -----------------------------------------


a="<a href='"
b="' target='_blank'>"
c="</a>"
d="https://www.ncbi.nlm.nih.gov/search/all/?term="
x=""

s=a+d+x+b+x+c


sop=data1.sort_values(by="reads", axis=0, ascending=False)
 
for i, row in sop.iterrows():
      
      x=str.lstrip(row[("organism")])
                 
      s=a+d+x+b+x+c
      
      sop.at[i,"organism"]=s


# Send df to HTML ------------------------------------------------------------

      
sop.to_html("zzz_test.html", render_links=True, escape=False,\
             justify=("left")) 
      
window.Close()

time.sleep(2)

webbrowser.open_new_tab("zzz_test.html")


# SNIPPET TRASH HEAP ---------------------------------------------------------

# window.Element("-FILE_PATH-").focus=True

# In PySimpleGUI there are 5 types of button configurations:
# button_type=5
# Yes, No: 1
# Cancel: 2
# Error: 3
# Ok, cancel: 4
# No button: 5