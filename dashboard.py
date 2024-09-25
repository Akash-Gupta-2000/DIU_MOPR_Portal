import streamlit as st
import utils

def show_dashboard():
    st.title("Dashboard")
    
    # Filter Options
    selected_state, selected_year = utils.render_filter_options()

    # Display KPI statistics and graphs for Dashboard
    st.subheader(f"📈 Dashboard: {selected_state} - {selected_year}")
    utils.display_kpi_stats(selected_state, selected_year)
    utils.display_graphs(selected_state, selected_year)
