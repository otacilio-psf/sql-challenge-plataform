import streamlit as st

class UI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title = "SQL Challenge"
        )
    
    def display_header_and_desc(self):
        st.title("SQL Challage #1")
        st.write("""
        ### #1 For the following tables: invoices and customers
        
        Select customer countries that contain the letter 'u' and total values (2 digits) where the total is greater than 100
        """)

    def display_query_area(self):
        self.query_input = st.text_area("Enter your query here:", height=300)

    def init_3_columns(self):
        return st.columns(3)

    def display_run_query_buttons(self):
        return st.button("Run query")

    def display_validate_query_button(self):
        return st.button("Validate result")

    def display_submit_button(self):
        return st.button("Submit solution")

    def display_msg(self, msg):
        st.write(msg)
    
    def display_success(self, msg):
        st.success(msg)

    def display_error(self, msg):
        st.error(msg)


if __name__ == "__main__":
    pass