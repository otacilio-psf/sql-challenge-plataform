from core.backend import ChallengeDB, BackendDB
from core.authentication import Authenticator
import streamlit as st
import logging

dbh = ChallengeDB()
backend = BackendDB()
auth = Authenticator(backend)

def login():
    auth.show_login_form()

def challenge_1():
    header = "SQL Challage #1"
    desc = """
        ### #1 For the following tables: invoice and customer
        
        Select customer countries that contain the letter 'a' where the total (2 digits precision) is greater than 100
        * Expected columns name country and total (case sensitive)
        """

    st.title(header)
    st.write(desc)

    
    query_input = st.text_area("Enter your query here:", height=300, value="SELECT * FROM customer")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        run_query = st.button("Run query")
    with col2:
        validate_query = st.button("Validate result")
    with col3:
        submit_solution = st.button("Submit solution")
    
    if run_query:
        try:
            df_result = dbh.retrive_results(query_input)
            df_result.style.format(precision=6)
            st.dataframe(df_result, hide_index=True)
        except dbh.invalid_query_exception as e:
            st.error("The query is invalid")
            logging.error(e)
        except TypeError as e:
            st.error("The query is invalid")
            logging.error(e)
        except Exception as e:
            st.exception(e)
            logging.error(e)

    elif validate_query:
        try:
            df_result = dbh.retrive_results(query_input)
            validation = dbh.compare_solution(query_input, "1")
            if validation:
                st.success("The result is correct")
                st.balloons()
            else:
                st.error("The result is incorrect")
        except dbh.invalid_query_exception as e:
            st.error("The query is invalid")
            logging.error(e)
        except TypeError as e:
            st.error("The query is invalid")
            logging.error(e)
        except Exception as e:
            st.exception(e)
            logging.error(e)
    
    elif submit_solution:
        df = dbh.retrive_results("EXPLAIN ANALYZE\n" + query_input)
        df = df[df.iloc[:, 0].str.contains('execution time:')]
        execution_time = df.iloc[:, 0].str.extract(r'(\d+)').iat[0, 0]
        backend.challenge_submission(1, st.session_state['user_email'], query_input, execution_time)
        st.success("Submitted")


login()
challenge_1()