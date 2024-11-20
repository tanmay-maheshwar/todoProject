FILE_PATH = "todos.txt"



def get_todos(filepath=FILE_PATH):
    """
    Reads the todos file and returns the list of todo
    items in it.
    """
    with open(filepath,'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local


def write_todos(todos_arg, filepath=FILE_PATH):
    """
    Takes the new todo list and writes it in the
    todo.txt file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)




