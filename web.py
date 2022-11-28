import streamlit as st
from backend import read_todos, write_todos

def add_todo():
    todos = read_todos()
    new_todo = st.session_state['new_todo']
    todos.append(new_todo)
    write_todos(todos)
    st.session_state['new_todo'] = ''

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your activity')

todos = read_todos()
for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(idx)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Input box', placeholder='Add a new todo',
            on_change=add_todo, 
            key='new_todo')

# st.session_state