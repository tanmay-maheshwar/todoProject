import functions
import FreeSimpleGUI as sg
import time
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



if not os.path.exists("todos.txt"):
    with open('todos.txt','w') as file:
        pass

sg.theme("DarkGrey11")

clock = sg.Text(time.strftime("%c"),key='time')
label = sg.Text("Type in to-do:")
user_input = sg.InputText(tooltip="Enter a todo",key="todo")
add_button = sg.Button(image_source=resource_path("add.png"),key="Add",tooltip="Add todo")


todos_list_display = sg.Listbox(values=functions.get_todos(), key = "todos_list", enable_events= True, size= (43,10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source = resource_path("complete.png"),key="Complete")
exit_button = sg.Button("Exit")



window = sg.Window("My To-Do App",layout=[[clock],
                                          [label],
                                          [user_input,add_button],
                                          [todos_list_display,edit_button,complete_button],
                                          [exit_button]])


while True:

    event, values = window.read(timeout=20)

    match event:
        case "Add":
            if values['todo'] != "":

                todos_list = functions.get_todos()
                todos_list.append(values['todo']+'\n')

                functions.write_todos(todos_list)
                window['todos_list'].update(values= todos_list)
                window['todo'].update(value='')

            else:
                sg.popup("Item is Empty!",font=("Helvetica",12))


        case "Edit":
            try:
                todos_list = functions.get_todos()
                new_todo = values['todo'] + '\n'
                old_todo_index = todos_list.index(values['todos_list'][0])
                todos_list[old_todo_index] = new_todo

                functions.write_todos(todos_list)
                window['todos_list'].update(values = todos_list)

                window['todo'].update(value = '')

            except IndexError:
                sg.popup("Please select an Item!",font=("Helvetica",12))


        case "Complete":
            try:
                complete_todo = values['todos_list'][0]
                todos_list = functions.get_todos()
                todos_list.remove(complete_todo)

                functions.write_todos(todos_list)

                window['todos_list'].update(values=todos_list)
                window['todo'].update(value='')

            except IndexError:
                sg.popup("Please select an Item!",font=("Helvetica",12))

        case "todos_list":
            window['todo'].update(value = values['todos_list'][0].strip())

        case sg.WINDOW_CLOSED:
            break


        case "Exit":
            break

    window['time'].update(value=time.strftime("%d,%b %I:%M:%S %p"))


window.close()

