import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in to-do:")
user_input = sg.InputText(tooltip="Enter a todo",key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",layout=[[label],[user_input,add_button]])

while True:

    event, values = window.read()
    match event:
        case "Add":
            todos_list = functions.get_todos()
            todos_list.append(values['todo']+'\n')

            functions.write_todos(todos_list)

        case sg.WINDOW_CLOSED:
            break



window.close()

