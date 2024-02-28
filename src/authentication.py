from backend import BackendDB
import streamlit as st
import bcrypt

class Authenticator:

    def __init__(self, backend):
        self._backend = backend

    def _login_form(self):
        if st.session_state.get('logged_in', False):
            return True
        with st.form('login'):
            st.subheader('Login')    
            st.text_input('Email', key='email').lower()
            st.text_input('Password', type='password', key='password')
            st.form_submit_button('Login', on_click=self._validate_login)
        st.button("Register", on_click=self.show_pre_authorization)

    def _validate_login(self):
        if self._backend.validate_email(st.session_state['email']):
            hash_password = self._backend.read_password(st.session_state['email']).encode()
            if bcrypt.checkpw(st.session_state['password'].encode(), hash_password):
                st.session_state['logged_in'] = True
                del st.session_state['password']
            else:
                st.error(f"Wrong password")
        else:
            st.error(f"Email '{st.session_state['email']}' is not registred")

    def show_login_form(self):
        if not self._login_form():
            st.stop()

    def _pre_authorization_form(self):
        if st.session_state.get('pre_authorized', False):
            return True
        with st.form('pre_authorized_verification'):
            st.subheader('Pre-authorized verification')    
            st.text_input('Email', key='pre_auth_email').lower()
            st.form_submit_button('Verify', on_click=self._check_pre_authorization)

    def _check_pre_authorization(self):
        if self._backend.validate_preauth_email(st.session_state['pre_auth_email']):
            st.session_state['pre_authorized'] = True
            self.show_registration_form()
        else:
            st.error(f"Email '{st.session_state['pre_auth_email']}' is not in the list")

    def show_pre_authorization(self):
        if not self._pre_authorization_form():
            st.stop()
        

    def _registration_form(self):
        if st.session_state.get('registration_submitted', False):
            return True
        with st.form('pre_authorized_registration'):
            st.subheader('Pre-authorized registration')
            st.text_input('Password', type='password', key='pre_auth_password')
            st.form_submit_button('Get Started', on_click=self._registration)
        return False

    def _registration(self):
        hash_pw = bcrypt.hashpw(st.session_state['pre_auth_password'].encode(), bcrypt.gensalt()).decode()
        del st.session_state['pre_auth_password']
        self._backend.upsert_user(st.session_state['pre_auth_email'], hash_pw)
        st.session_state['registration_submitted'] = True
        
    def show_registration_form(self):
        if not self._registration_form():
            st.stop()


if __name__ == '__main__':
    backend = BackendDB()
    auth = Authenticator(backend)
    auth.show_login_form()
    st.write(st.session_state['email'])
    st.write("# It works!")
