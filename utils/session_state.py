import streamlit as st

def get_manager():
    if "manager" not in st.session_state:
        from models.task_manager import Task_Manager
        st.session_state.manager = Task_Manager()
    return st.session_state.manager
    
