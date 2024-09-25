import streamlit as st
import utils

def show_fto_analysis():
    st.title("FTO Analysis")
    
    # Filter Options
    selected_state, selected_year = utils.render_filter_options()

    # Display KPI statistics and graphs for FTO Tab
    st.subheader(f"📊 FTO Tab: {selected_state} - {selected_year}")
    utils.display_kpi_stats(selected_state, selected_year)
    utils.display_graphs(selected_state, selected_year)
