import streamlit as st
import bcrypt


class Authenticator:

    def __init__(self):
        pass

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
        ## Validation logic with backend
        mock_mail_list = ['test']

        if st.session_state['email'] in mock_mail_list:
            mock_pw = bcrypt.hashpw("test".encode(), bcrypt.gensalt())
            if bcrypt.checkpw(st.session_state['password'].encode(), mock_pw):
                st.session_state['logged_in'] = True
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
        email_list = ['test'] # get the email list from backend
        if st.session_state['pre_auth_email'] in email_list:
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
        hash_pw = bcrypt.hashpw(st.session_state['pre_auth_password'].encode(), bcrypt.gensalt())
        del st.session_state['pre_auth_password']
        
        # connect to the backend and save st.session_state['pre_auth_email'] and hash_pw

        st.session_state['registration_submitted'] = True
        
    def show_registration_form(self):
        if not self._registration_form():
            st.stop()


if __name__ == '__main__':
    auth = Authenticator()
    auth.show_login_form()
    st.write(st.session_state['email'])
    st.write("# It works!")
