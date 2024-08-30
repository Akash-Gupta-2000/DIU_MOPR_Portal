import streamlit as st
import os
from PIL import Image
import pandas as pd

# Define the base directory for the graphs
BASE_DIR = "State"

# Get the list of states from the base directory
states = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]

# Create dropdown for selecting state in the sidebar
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
st.write(f"## Key Performance Indicators for {selected_state} - {selected_year}")

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
    st.table(kpi_df)
else:
    st.write("No KPI data available for the selected year.")

# Get the path of the selected financial year
graphs_path = os.path.join(BASE_DIR, selected_state, selected_year)

# Get the list of graphs for the selected state and financial year
graphs = [g for g in os.listdir(graphs_path) if os.path.isfile(os.path.join(graphs_path, g))]

# Display all graphs
st.write(f"## Graphs for {selected_state} - {selected_year}")

for graph in graphs:
    graph_file_path = os.path.join(graphs_path, graph)
    image = Image.open(graph_file_path)
    st.image(image, caption=graph, use_column_width=True)
