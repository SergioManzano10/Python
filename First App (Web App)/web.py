import streamlit as st
import Functions

todos = Functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n" 
    todos.append(todo)
    Functions.write_todos(todos)



st.title("My todo App")
st.subheader("This is the web app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = "", placeholder = "Add new todo...", on_change = add_todo, key = "new_todo") 