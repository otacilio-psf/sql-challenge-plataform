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
        ### Code Wars: The Digital Mafia Chronicles
        
        As a digital citizen of the Data Hub, you've got to navigate the mean streets where different data clans roam. One day you're a data point, the next day you’re an outlier.​

        The bigwigs of mafia families have called a summit to battle for the ultimate treasure: the next Gold rush—computing power. It's the scarce resource that keeps their digital mafia operations running smoothly.

        Your initiation ritual in the mafia is to gain as much Computer power for your clan as possible.​
        
        Each Computer power cluster will be assigned to a mafia clan once there is someone from a different clan requesting for Computer power.
        
        Create the Godquery to rank the Mafia clans based on their computer power (number of clusters).​

        Instructions:
        - You should always read from the **dataset** table
        - Your final collumns need to have the name department and count, case sensitive
        - The query need to work for the 4 scenarios, to run for each case you just need to click in the "Run query for ..."
        """

    st.title(header)
    st.write(desc)

    img1, img2, img3 = st.columns([1,1,1])

    img1.image("src/pages/page_elements/ch-1-example.png")
    img2.image("src/pages/page_elements/arrow.png")
    img3.image("src/pages/page_elements/ch-1-expected.png")

   
    query_input = st.text_area("Enter your query here:", height=300, value="SELECT * FROM dataset")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        run_query_1 = st.button("Run query for ds 1")
        run_query_2 = st.button("Run query for ds 2")
        run_query_3 = st.button("Run query for ds 3")
        run_query_4 = st.button("Run query for ds 4")
    with col2:
        validate_query = st.button("Validate result")
    with col3:
        submit_solution = st.button("Submit solution")
    
    def run_query(query_input, ds):
        try:
            query_input = query_input.replace("dataset", ds)
            df_result = dbh.retrive_results(query_input)
            st.dataframe(df_result, hide_index=True, use_container_width=True)
        except dbh.invalid_query_exception as e:
            st.error("The query is invalid")
            logging.error(e)
        except TypeError as e:
            st.error("The query is invalid")
            logging.error(e)
        except Exception as e:
            st.exception(e)
            logging.error(e)

    if run_query_1:
        run_query(query_input, "challenge1_dataset1")
    elif run_query_2:
        run_query(query_input, "challenge1_dataset2")
    elif run_query_3:
        run_query(query_input, "challenge1_dataset3")
    elif run_query_4:
        run_query(query_input, "challenge1_dataset4")

    elif validate_query:
        st.info("Need to reimplement")
        # try:
        #     df_result = dbh.retrive_results(query_input)
        #     validation = dbh.compare_solution(query_input, "1")
        #     if validation:
        #         st.success("The result is correct")
        #         st.balloons()
        #     else:
        #         st.error("The result is incorrect")
        # except dbh.invalid_query_exception as e:
        #     st.error("The query is invalid")
        #     logging.error(e)
        # except TypeError as e:
        #     st.error("The query is invalid")
        #     logging.error(e)
        # except Exception as e:
        #     st.exception(e)
        #     logging.error(e)
    
    elif submit_solution:
        st.info("Need to reimplement")
        # df = dbh.retrive_results("EXPLAIN ANALYZE\n" + query_input)
        # df = df[df.iloc[:, 0].str.contains('execution time:')]
        # execution_time = df.iloc[:, 0].str.extract(r'(\d+)').iat[0, 0]
        # backend.challenge_submission(1, st.session_state['user_email'], query_input, execution_time)
        # st.success("Submitted")


login()
challenge_1()