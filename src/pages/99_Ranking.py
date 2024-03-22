from core.authentication import Authenticator
from core.backend import BackendDB
import streamlit as st

backend = BackendDB()
auth = Authenticator(backend)

def login():
    auth.show_login_form()

def highlight_medals(s):
    if s.name == 0:
        return ['background-color: #FFD700'] * len(s)  # Gold
    elif s.name == 1:
        return ['background-color: #C0C0C0'] * len(s)  # Silver
    elif s.name == 2:
        return ['background-color: #CD7F32'] * len(s)  # Bronze
    else:
        return [''] * len(s)

def challenge_1():
    st.write("### Challenge 1")
    df = backend.get_submission(1)
    
    st.write("#### Best Execution Time")
    df_time = df[["email","execution_time_ms", "submission_datetime"]]
    df_time = df_time.sort_values(by=['execution_time_ms', 'submission_datetime']).reset_index(drop=True)
    st.dataframe(df_time.style.apply(highlight_medals, axis=1), hide_index=True, use_container_width=True)


    st.write("#### Best Memory Usage")
    df_memory = df[["email","max_memory_usage_mib", "submission_datetime"]]
    df_memory = df_memory.sort_values(by=['max_memory_usage_mib', 'submission_datetime']).reset_index(drop=True)
    st.dataframe(df_memory.style.apply(highlight_medals, axis=1), hide_index=True, use_container_width=True)
    

def home():
    header = "SQL Challage Ranking"
    st.title(header)
    challenge_1()

login()
home()