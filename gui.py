import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in to-do:")
user_input = sg.InputText(tooltip="Enter a todo",key="todo")
add_button = sg.Button("Add")
todos_list_display = sg.Listbox(values=functions.get_todos(), key = "todos_list", enable_events= True, size= (43,10))
edit_button = sg.Button("Edit")


window = sg.Window("My To-Do App",layout=[[label],
                                          [user_input,add_button],
                                          [todos_list_display,edit_button]])

while True:

    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos_list = functions.get_todos()
            todos_list.append(values['todo']+'\n')

            functions.write_todos(todos_list)
            window['todos_list'].update(values= todos_list)
            window['todo'].update(value='')


        case "Edit":
            todos_list = functions.get_todos()
            new_todo = values['todo'] + '\n'
            old_todo_index = todos_list.index(values['todos_list'][0])
            todos_list[old_todo_index] = new_todo

            functions.write_todos(todos_list)
            window['todos_list'].update(values = todos_list)

            window['todo'].update(value = '')

        case "todos_list":
            window['todo'].update(value = values['todos_list'][0].strip())


        case sg.WINDOW_CLOSED:
            break



window.close()

