from core.authentication import Authenticator
from core.backend import BackendDB
from core.utilities import get_funny_name
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
    try:
        st.write("### Challenge 1")
        df = backend.get_submission(1)
        
        st.write("#### Best Execution Time")
        df_time = df[["email","execution_time_ms", "submission_datetime"]]
        df_time = df_time.sort_values(by=['execution_time_ms', 'submission_datetime']).drop_duplicates(subset=['email'], keep='first').reset_index(drop=True)
        st.dataframe(df_time.style.apply(highlight_medals, axis=1), hide_index=True, use_container_width=True)


        st.write("#### Best Total Cost")
        df_memory = df[["email","total_cost", "submission_datetime"]]
        df_memory = df_memory.sort_values(by=['total_cost', 'submission_datetime']).drop_duplicates(subset=['email'], keep='first').reset_index(drop=True)
        st.dataframe(df_memory.style.apply(highlight_medals, axis=1), hide_index=True, use_container_width=True)
    except KeyError:
        st.info("No subssions yet")
    except Exception as e:
        st.exception(e)
    

def home():
    header = "SQL Challage Ranking"
    st.title(header)
    st.info(f"Your name: {st.session_state['user_email']}")
    challenge_1()

#login()
get_funny_name()
home()