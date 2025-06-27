import streamlit as st
import pandas as pd

# Load Excel file
df = pd.read_excel('parts.xlsx')

st.title("Parts Query Chatbot")

# User input
query = st.text_input("Enter Part Number or Description:")

# Search logic
if query:
    result = df[
        df['Part Number'].astype(str).str.contains(query, case=False) |
        df['Description'].str.contains(query, case=False)
    ]
    
    if not result.empty:
        st.write("Search Results:")
        st.dataframe(result)
    else:
        st.write("No matching part found.")
