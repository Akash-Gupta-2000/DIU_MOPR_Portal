import streamlit as st
import os
from PIL import Image
import pandas as pd

# Set the app title and a header
st.set_page_config(page_title="Manthan KPI Dashboard", layout="wide")
st.title("📊 Manthan KPI Dashboard")

# Add a custom description
st.markdown("""
Welcome to the Manthan Dashboard. Here, you can explore key performance indicators (KPIs) and graphs 
for different states and financial years. Use the sidebar to select the state and year.
""")

# Define the base directory for the graphs
BASE_DIR = "State"

# Get the list of states from the base directory
states = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]

# Create dropdown for selecting state in the sidebar
st.sidebar.header("🔍 Filter Options")
selected_state = st.sidebar.selectbox("Select State", states)

# Get the list of financial years for the selected state
financial_years = [fy for fy in os.listdir(os.path.join(BASE_DIR, selected_state)) if os.path.isdir(os.path.join(BASE_DIR, selected_state, fy))]

# Create dropdown for selecting financial year in the sidebar
selected_year = st.sidebar.selectbox("Select Financial Year", financial_years)

# Dictionary to store KPI statistics for each financial year
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

# Display KPI statistics for the selected financial year
st.subheader(f"📈 Key Performance Indicators: {selected_state} - {selected_year}")

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

# Get the path of the selected financial year
graphs_path = os.path.join(BASE_DIR, selected_state, selected_year)

# Get the list of graphs for the selected state and financial year
graphs = [g for g in os.listdir(graphs_path) if os.path.isfile(os.path.join(graphs_path, g))]

# Display all graphs
st.subheader(f"📊 Graphs: {selected_state} - {selected_year}")

if graphs:
    col1, col2 = st.columns(2)  # Display in two columns
    for i, graph in enumerate(graphs):
        graph_file_path = os.path.join(graphs_path, graph)
        image = Image.open(graph_file_path)
        
        # Display graphs in alternating columns
        caption_text = f"Graph: {graph.split('.')[0]}"
        
        # Display graphs in alternating columns
        if i % 2 == 0:
            with col1:
                st.image(image, caption=None, use_column_width=True)
                st.markdown(f"<div style='text-align:center; margin-top:10px; font-size:16px; font-weight:bold;'>{caption_text}</div>", unsafe_allow_html=True)
        else:
            with col2:
                st.image(image, caption=None, use_column_width=True)
                st.markdown(f"<div style='text-align:center; margin-top:10px; font-size:16px; font-weight:bold;'>{caption_text}</div>", unsafe_allow_html=True)
        
        # Add vertical space between images
        st.markdown("<div style='margin-bottom:30px;'></div>", unsafe_allow_html=True)
else:
    st.warning("No graphs available for the selected year.")
