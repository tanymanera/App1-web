FILE_PATH = 'todos.txt'

def write_todos(todos_list):
    ''' Append at every item of todo_list a new-line
    and save the list on todos.txt'''
    todos_list = [todo + '\n' for todo in todos_list]
    with open( FILE_PATH, 'w') as file:
        file.writelines(todos_list)


def read_todos(path=FILE_PATH):
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
        todos = [todo.strip() for todo in todos]
    return todos
