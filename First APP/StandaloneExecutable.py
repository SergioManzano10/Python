import PySimpleGUI as PSG
import Functions
import time 
import os # Sirve para que el programa sea independiente del archivo todos.txt

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


PSG.theme("Material1") 

label = PSG.Text("Type in a to-do")
clock = PSG.Text("", key = "clock")
input_box = PSG.InputText(tooltip = "Enter a todo", key = "newval") 
add_button = PSG.Button("Add")

label2 = PSG.Text("Choose a to-do")
list_box = PSG.Listbox(values = Functions.get_todos(), key = "existing todos", enable_events = True, size = [45, 10])
edit_button = PSG.Button("Edit")
remove_button = PSG.Button("Remove")
exit_button = PSG.Button("Exit")

window = PSG.Window("My To-Do App", layout=[[clock], [label, input_box, add_button], [[label2, list_box, edit_button, remove_button]], [exit_button]], font = ("Helvetica", 13)) 

while True: 
    event, values = window.read(timeout=200) 
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S")) 
    match event:
        case "Add":
            todos = Functions.get_todos()
            new_todo = values["newval"] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
            window["existing todos"].update(values=todos) 

        case "Edit":
            try:
                todo_to_edit = values["existing todos"][0]
                new_todo = values["newval"]

                todos = Functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                Functions.write_todos(todos)
                window["existing todos"].update(values=todos) 

            except IndexError:
                PSG.popup("Please, select an item first", font = ("Helvetica", 13)) 
        
        case "Remove":
            try:
                todo_to_remove = values["existing todos"][0]

                todos = Functions.get_todos()
                todos.remove(todo_to_remove) 
                Functions.write_todos(todos)
                window["existing todos"].update(values = todos)
                window["newval"].update(value = "")

            except IndexError:
                PSG.popup("Please, select an item first", font = ("Helvetica", 13)) 
        
        case "existing todos": 
            window["newval"].update(value=values["existing todos"][0])

        case "Exit":
            break

        case PSG.WIN_CLOSED: 
            break

window.close()