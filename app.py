
import streamlit as st
import pandas as pd

st.title("PK's Parts Chatbot")

# Load data
df = pd.read_excel("parts.xlsx")

# Search box
query = st.text_input("Hello, Welcome.  Please Enter part number or description:")

# Show results
if query:
    results = df[df['Part No'].astype(str).str.contains(query, case=False) |
                 df['Part Desc'].str.contains(query, case=False)]
    if not results.empty:
        st.write(results)
    else:
        st.write("No matching parts found.")
