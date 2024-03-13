from core.authentication import Authenticator
from core.backend import BackendDB
import streamlit as st

backend = BackendDB()
auth = Authenticator(backend)

def home():
    st.markdown("""
    ## Welcome to the SQL Challenge Platform!

    To gain access, you must use your company email. Please proceed by clicking on the registration button to register your email and create your password.

    In the event that you forget your password, don't worry! You can simply register again to generate a new one.
    """)

    col1, col2, col3 = st.columns([1, 1, 4])

    with col1:
        st.button("Register", on_click=auth.show_pre_authorization)
    with col2:
        st.button("Login", on_click=auth.show_login_form)

home()