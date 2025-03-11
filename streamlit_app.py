# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

helpful_links = [
    "https://docs.streamlit.io",
    "https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit",
    "https://github.com/Snowflake-Labs/snowflake-demo-streamlit",
    "https://docs.snowflake.com/en/release-notes/streamlit-in-snowflake"
]

# Write directly to the app
st.title("My Parents New Healthy Diner")
st.title("Breakfast Menu")
st.write(
    f"""
    Omega 3 & Blue Berry Oatmeal

    Kale, Spinach & Rocket Smoothie
    
    Hard-Boiled Free-Range Egg
    """
)