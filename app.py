
import streamlit as st
import pandas as pd

st.title("Parts Chatbot")

# Load data
df = pd.read_excel("parts.xlsx")

# Search box
query = st.text_input("Enter part number or description:")

# Show results
if query:
    results = df[df['Part Number'].astype(str).str.contains(query, case=False) | 
                 df['Description'].str.contains(query, case=False)]
    if not results.empty:
        st.write(results)
    else:
        st.write("No matching parts found.")
