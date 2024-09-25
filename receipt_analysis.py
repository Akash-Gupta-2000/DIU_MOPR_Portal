import streamlit as st
import utils

def show_receipt_analysis():
    st.title("Receipt Analysis")
    
    # Filter Options
    selected_state, selected_year = utils.render_filter_options()

    # Display KPI statistics and graphs for Receipt Analysis
    st.subheader(f"📊 Receipt Analysis: {selected_state} - {selected_year}")
    utils.display_kpi_stats(selected_state, selected_year)
    utils.display_graphs(selected_state, selected_year)
