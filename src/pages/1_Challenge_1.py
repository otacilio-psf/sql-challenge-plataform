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
        - Your final result should have two columns, department and computer_power
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
            if type(e).__name__ == "ProgrammingError":
                st.error("The query is invalid")
            else:
                st.exception(e)
                logging.error(e)

    def validate_input_query(query_input, ds, silent=False):
        try:
            ds_number = ds.split('.')[0].split('dataset')[-1]
            query_input = query_input.replace("dataset", ds)
            validation = dbh.compare_solution(query_input, ds)
            if validation:
                st.session_state[f'{ds}_validation'] = True
                if not silent:
                    st.success(f"The result is correct for dataset {ds_number}")
            else:
                st.session_state[f'{ds}_validation'] = False
                st.error(f"The result is incorrect for dataset {ds_number}")
        except dbh.invalid_query_exception as e:
            st.session_state[f'{ds}_validation'] = False
            st.error("The query is invalid")
            logging.error(e)
        except TypeError as e:
            st.session_state[f'{ds}_validation'] = False
            st.error("The query is invalid")
            logging.error(e)
        except Exception as e:
            st.session_state[f'{ds}_validation'] = False
            if type(e).__name__ == "ProgrammingError":
                st.error("The query is invalid")
            else:
                st.exception(e)
                logging.error(e)
        
    if run_query_1:
        with st.spinner('Please wait...'):
            run_query(query_input, "challenge1_dataset1")
    elif run_query_2:
        with st.spinner('Please wait...'):
            run_query(query_input, "challenge1_dataset2")
    elif run_query_3:
        with st.spinner('Please wait...'):
            run_query(query_input, "challenge1_dataset3")
    elif run_query_4:
        with st.spinner('Please wait...'):
            run_query(query_input, "challenge1_dataset4")

    elif validate_query:
        with st.spinner('Please wait...'):
            validate_input_query(query_input, "challenge1_dataset1")
            validate_input_query(query_input, "challenge1_dataset2")
            validate_input_query(query_input, "challenge1_dataset3")
            validate_input_query(query_input, "challenge1_dataset4")
            if all(st.session_state.get(f'challenge1_dataset{i}_validation', False) for i in range(1,5)):
                st.balloons()
    
    elif submit_solution:
        with st.spinner('Please wait...'):
            validate_input_query(query_input, "challenge1_dataset1", silent=True)
            validate_input_query(query_input, "challenge1_dataset2", silent=True)
            validate_input_query(query_input, "challenge1_dataset3", silent=True)
            validate_input_query(query_input, "challenge1_dataset4", silent=True)
            if all(st.session_state.get(f'challenge1_dataset{i}_validation', False) for i in range(1,5)):
                query_input = query_input.replace("dataset", "challenge1_dataset4")
                df = dbh.retrive_results("EXPLAIN ANALYZE\n" + query_input)
                
                df_total_cost = df['QUERY PLAN'].str.extract(r"cost=(\d+\.\d+\.\.\d+\.\d+)")
                total_cost = float(df_total_cost.iloc[0, 0].split('..')[-1])

                execution_time = df[df['QUERY PLAN'].str.contains('Execution Time')].iloc[0,0]
                execution_time = execution_time.split(": ")[-1]
                if execution_time.endswith(" ms"):
                    execution_time = float(execution_time.replace(" ms", ""))
                elif execution_time.endswith(" s"):
                    execution_time = float(execution_time.replace(" s", "")) * 1000
                elif execution_time.endswith(" µs"):
                    execution_time = float(execution_time.replace(" µs", "")) / 1000
                else:
                    raise Exception("time unit not expected")

                backend.challenge_submission(1, st.session_state['user_email'], query_input, execution_time, total_cost)
                st.success("Submitted")
            else:
                st.error("The query don't work for all validations")


login()
challenge_1()