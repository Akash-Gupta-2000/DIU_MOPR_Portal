import streamlit as st
import os
import pandas as pd
from PIL import Image

BASE_DIR = "State"

# Utility function to render filter options
def render_filter_options():
    states = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]
    
    # Create two columns for the dropdowns
    col1, col2 = st.columns(2)
    
    with col1:
        selected_state = st.selectbox("Select State", states)

    with col2:
        financial_years = [fy for fy in os.listdir(os.path.join(BASE_DIR, selected_state)) if os.path.isdir(os.path.join(BASE_DIR, selected_state, fy))]
        selected_year = st.selectbox("Select Financial Year", financial_years)
    
    return selected_state, selected_year

# Utility function to display KPI stats
def display_kpi_stats(selected_state, selected_year):
    # Mock KPI stats for demonstration
    kpi_stats = {
        "2022-23": {
            "Number of Duplicate Transactions": 47864,
            "Number of Unique Duplicate Transactions": 20345,
            "Total Revenue Due to Duplicate Transactions": 412797710.29
        },
        "2023-24": {
            "Number of Duplicate Transactions": 26766,
            "Number of Unique Duplicate Transactions": 11597,
            "Total Revenue Due to Duplicate Transactions": 290331826.61
        }
    }
    
    if selected_year in kpi_stats:
        kpi_data = {
            "Description": [
                "Number of Duplicate Transactions",
                "Number of Unique Duplicate Transactions",
                "Total Revenue Due to Duplicate Transactions"
            ],
            "Figures": [
                f"{kpi_stats[selected_year]['Number of Duplicate Transactions']:,}",
                f"{kpi_stats[selected_year]['Number of Unique Duplicate Transactions']:,}",
                f"₹{kpi_stats[selected_year]['Total Revenue Due to Duplicate Transactions'] / 10**7:,.2f} Crore"
            ]
        }
        kpi_df = pd.DataFrame(kpi_data)
        kpi_df.index = kpi_df.index + 1
        st.table(kpi_df.style.set_properties(**{
            'background-color': '#f0f2f6',
            'color': 'black',
            'border-color': 'black',
            'text-align': 'center'
        }))
    else:
        st.warning("No KPI data available for the selected year.")

# Utility function to display graphs
def display_graphs(selected_state, selected_year):
    graphs_path = os.path.join(BASE_DIR, selected_state, selected_year)
    graphs = [g for g in os.listdir(graphs_path) if os.path.isfile(os.path.join(graphs_path, g))]

    if graphs:
        col1, col2 = st.columns(2)  # Display in two columns
        for i, graph in enumerate(graphs):
            graph_file_path = os.path.join(graphs_path, graph)
            image = Image.open(graph_file_path)

            # Display graphs in alternating columns
            caption_text = f"Graph: {graph.split('.')[0]}"
            
            if i % 2 == 0:
                with col1:
                    st.image(image, caption=None, use_column_width=True)
                    st.markdown(f"<div style='text-align:center; margin-top:10px; font-size:16px; font-weight:bold;'>{caption_text}</div>", unsafe_allow_html=True)
            else:
                with col2:
                    st.image(image, caption=None, use_column_width=True)
                    st.markdown(f"<div style='text-align:center; margin-top:10px; font-size:16px; font-weight:bold;'>{caption_text}</div>", unsafe_allow_html=True)
            
            st.markdown("<div style='margin-bottom:30px;'></div>", unsafe_allow_html=True)
    else:
        st.warning("No graphs available for the selected year.")
