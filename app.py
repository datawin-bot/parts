
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Interactive Parts Chatbot")

st.title("Interactive Parts Chatbot")

# Load data
df = pd.read_excel("parts.xlsx")

# Sidebar filters (optional)
with st.sidebar:
    st.write("**Filter Options**")
    location = st.selectbox("Select Location", ["All"] + sorted(df['Location 1'].dropna().unique().tolist()))

# Search box
query = st.text_input("🔎 Enter part number or description:")

# Filter based on query and location
filtered_df = df.copy()

if location != "All":
    filtered_df = filtered_df[filtered_df['Location 1'] == location]

if query:
    filtered_df = filtered_df[
        filtered_df['Part No'].astype(str).str.contains(query, case=False) |
        filtered_df['Part Desc'].str.contains(query, case=False)
    ]

# Show results
st.write("---")
if not filtered_df.empty:
    st.success(f"Found {len(filtered_df)} matching parts:")
    st.dataframe(filtered_df)
else:
    st.info("No matching parts found.")

st.write("---")
st.caption("Powered by Streamlit - Interactive Chatbot Example")
