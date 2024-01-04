# To use the program you need to download "zip_extractor_function.py"

import PySimpleGUI as PSG
from zip_extractor_function import extract_archive

PSG.theme("Material1") 

label1 = PSG.Text("Select archive:")
input1 = PSG.Input() 
choose_button1 = PSG.FileBrowse("Choose", key = "archive") # Es FileBrowse en singular porque solo queremos que el usuario seleccione una

label2 = PSG.Text("Select dest dir:")
input2 = PSG.Input() 
choose_button2 = PSG.FolderBrowse("Choose", key = "folder")

extract_button = PSG.Button("Extract")
output_label = PSG.Text(key = "output", text_color = "green")

window = PSG.Window("Archive Extractor", layout=([[label1, input1, choose_button1], 
                                                [label2, input2, choose_button2]],
                                                [extract_button, output_label]))


while True:
    event, values = window.read()
    print(event, values)
    archive_path = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archive_path, dest_dir)
    window["output"].update(value = "Extraction Completed")

window.close()