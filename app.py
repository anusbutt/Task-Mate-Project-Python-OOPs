import streamlit as st
from utils.session_state import get_manager

st.set_page_config(page_title="TaskMate", layout="centered")

st.title("TaslMate - Smart Task Manager")

manager = get_manager()

tab1, tab2, tab3 = st.tabs(["➕ Add Task", "📋 View Task", "👤 Manage Users"])

with tab3:
    st.subheader("Add New User")
    new_user = st.text_input("Username")

    if st.button("Add New User"):
        manager.add_user(new_user)
        st.success(f"User {new_user} added")

with tab1:
    st.subheader("Assign a New Task")
    users = manager.get_user()
    if users:
        selected_user = st.selectbox("Select User", users)
        title = st.text_input("Task Title")
        desc = st.text_area("Task Description")
        if st.button("Create Task"):
            task = manager.create_task(selected_user, title, desc)
            if task:
                st.success(f"Task Assign to {selected_user}.")
            else:
                st.error("Something Went Wrong.")

    else: 
        st.warning("Please Add a User First.")

with tab2:
    st.subheader("Tasks by Users")
    users = manager.get_user()
    if users:
        selected_user = st.selectbox("Select user to view task", users, key="view_user")
        tasks = manager.get_user_task(selected_user)
        for task in tasks:
            cols = st.columns([0.7, 0.3])
            with cols[0]:
                st.write(str(task))
            with cols[1]:
                if not task.completed:
                    if st.button(f"Mark Complete ✅", key=task.id):
                        task.mark_completed()
                        st.rerun()
    else:
        st.info("No User Available")

