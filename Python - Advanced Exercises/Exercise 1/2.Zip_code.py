# To use the program you need to download "zip_creator.py"

import PySimpleGUI as PSG
from zip_creator import make_archive

label1 = PSG.Text("Select files to compress:")
input1 = PSG.Input(tooltip = "Select the files") 
add_button1 = PSG.FilesBrowse("Choose", key = "files") 

label2 = PSG.Text("Select destination folder:")
input2 = PSG.Input(tooltip = "Select the files") 
add_button2 = PSG.FolderBrowse("Choose", key = "folder") 

compress_Button = PSG.Button("Compress")
output_label = PSG.Text (key = "output")

window = PSG.Window("File Compressor", layout=([[label1, input1, add_button1], 
                                                [label2, input2, add_button2]],
                                                [compress_Button, output_label]))

while True:
    event, values = window.read()
    print(event, values) 
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value = "Compression completed" )

window.close()