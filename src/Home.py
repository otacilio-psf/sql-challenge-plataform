from core.authentication import Authenticator
from core.backend import BackendDB
import streamlit as st

backend = BackendDB()
auth = Authenticator(backend)

def home():
    st.info("WIP")
    st.markdown("""
    ## Welcome to the SQL Challenge Platform!

    To gain access, you must be pre-authorized. Once your email is on the approved list, please proceed by clicking on the registration button to create your password.

    In the event that you forget your password, don't worry! You can simply register again to generate a new one.
    """)

    st.button("Register", on_click=auth.show_pre_authorization)

home()