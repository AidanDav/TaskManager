import streamlit as st
from task_manager import TaskManager

if "manager" not in st.session_state:
    st.session_state.manager = TaskManager()
manager = st.session_state.manager

st.title("Task Manager")


#add a new task
st.header("Add a New Task")
name = st.text_input("Task Name")
description = st.text_area("Task Description")
due_date = st.date_input("Due Date")

if st.button("Add Task"):
    if name.strip():
        manager.add_task(name, description, due_date)
        st.success("Task added successfully!")
    else:
        st.warning("Task name cannot be empty.")

#show tasks 
st.header("Current Tasks")
tasks = manager.list_tasks()

if not tasks:
    st.info("No tasks available. Please add a task.")
else:
    for task in tasks:
        st.subheader(task.name)
        st.write(f"Description: {task.description}")
        st.write(f"Due Date: {task.due_date.strftime('%Y-%m-%d')}")
        st.write(f"Status: {'Completed' if task.completed else 'Pending'}")
        st.write(f"Times Done: {task.times_done}")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button(f"Complete Task {task.id}"):
                manager.complete_task(task.id)
                st.rerun()
        with col2:
            if st.button(f"Delete Task {task.id}"):
                manager.delete_task(task.id)
                st.rerun()
        with col3:
            if st.button(f"Increment Times Done {task.id}"):
                manager.increment_task_times_done(task.id)
                st.rerun()