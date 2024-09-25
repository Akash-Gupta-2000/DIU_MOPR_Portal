import streamlit as st
import utils

def show_expenditure_analysis():
    st.title("Expenditure Analysis")
    
    # Filter Options
    selected_state, selected_year = utils.render_filter_options()

    # Display KPI statistics and graphs for Expenditure Analysis
    st.subheader(f"📊 Expenditure Analysis: {selected_state} - {selected_year}")
    utils.display_kpi_stats(selected_state, selected_year)
    utils.display_graphs(selected_state, selected_year)
