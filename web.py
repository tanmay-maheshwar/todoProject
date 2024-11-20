import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local+'\n')
    functions.write_todos(todos)





st.title("My Todo App")
st.subheader("This is a app for recording todos.")

for todo in todos:
    st.checkbox(todo)


st.text_input(label="",placeholder="Add new todo",on_change=add_todo,key="new_todo")



st.session_state
