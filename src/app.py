from frontend import UI

def main():
    ui = UI()

    ui.display_header_and_desc()
    ui.display_query_area()
    
    col1, col2, col3 = ui.init_3_columns()
    with col1:
        run_query = ui.display_run_query_buttons()
    with col2:
        validate_query = ui.display_validate_query_button()
    with col3:
        submit_solution = ui.display_submit_button()
    
    if run_query:
        ui.display_error(f"Run not implemented yet | Input: {ui.query_input}")
    elif validate_query:
        ui.display_error(f"Validation not implemented yet | Input: {ui.query_input}")
    elif submit_solution:
        ui.display_error(f"Submission not implemented yet | Input: {ui.query_input}")

if __name__ == "__main__":
    main()