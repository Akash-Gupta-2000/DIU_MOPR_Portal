import streamlit as st
import dashboard
import receipt_analysis
import expenditure_analysis
import fto_analysis

# Set the app title and layout
st.set_page_config(page_title="Manthan KPI Dashboard", layout="wide")

# Create session state to keep track of the selected tab
if 'selected_tab' not in st.session_state:
    st.session_state.selected_tab = 'Dashboard'

# CSS styles for radio buttons
st.markdown(
    """
    <style>
    .stRadio > label {
        font-size: 24px; /* Increase the font size */
        font-weight: bold; /* Bold text */
        padding: 10px; /* Padding around the text */
    }
    </style>
    """, unsafe_allow_html=True
)

# Sidebar radio buttons for navigation
selected_tab = st.sidebar.radio(
    "",
    ["Dashboard", "Receipt Analysis", "Expenditure Analysis", "FTO Analysis"],
    index=["Dashboard", "Receipt Analysis", "Expenditure Analysis", "FTO Analysis"].index(st.session_state.selected_tab)
)

# Update the session state with the selected tab
st.session_state.selected_tab = selected_tab

# Main content based on the selected tab
if selected_tab == "Dashboard":
    dashboard.show_dashboard()
elif selected_tab == "Receipt Analysis":
    receipt_analysis.show_receipt_analysis()
elif selected_tab == "Expenditure Analysis":
    expenditure_analysis.show_expenditure_analysis()
elif selected_tab == "FTO Analysis":
    fto_analysis.show_fto_analysis()
