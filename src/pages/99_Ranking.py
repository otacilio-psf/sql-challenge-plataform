from core.authentication import Authenticator
from core.backend import BackendDB
import streamlit as st

backend = BackendDB()
auth = Authenticator(backend)

def login():
    auth.show_login_form()

def home():
    st.info("Need to implement")

login()
home()