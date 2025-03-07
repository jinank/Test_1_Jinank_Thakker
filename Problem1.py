import pandas as pd
import streamlit as st
import plotly.express as px

# Load the flight data

flight_data = pd.read_csv('flight_data.csv')

# Display basic info
st.write("## Flight Data Exploration")
st.write(flight_data.head())

# --- Sidebar for filtering ---
st.sidebar.header("Filters")

# --- DIRECT ROUTES FROM JFK ---
jfk_routes = flight_data[flight_data['origin'] == 'JFK']
st.write("## JFK Routes")
st.write(jfk_routes[['origin', 'dest']].drop_duplicates())
