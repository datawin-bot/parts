import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Page configuration
st.set_page_config(page_title="Parts Chatbot", page_icon="🛠️", layout="centered")
st.title("🛠️ Parts Chatbot")

# Load data
@st.cache_data
def load_data():
    return pd.read_excel("parts.xlsx")

df = load_data()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask about a part number or description...")
if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot reply
    with st.chat_message("assistant"):
        # Fuzzy match the query
        matches = []
        for idx, row in df.iterrows():
            part_no_score = fuzz.partial_ratio(prompt.lower(), str(row['Part No']).lower())
            desc_score = fuzz.partial_ratio(prompt.lower(), str(row['Part Desc']).lower())
            if max(part_no_score, desc_score) > 70:
                matches.append(row)

        if matches:
            result_df = pd.DataFrame(matches)
            st.session_state.messages.append({"role": "assistant", "content": "Hi, Thanks for the Enquiry. Here are some matching parts:"})
            st.write(result_df)
        else:
            reply = "Sorry, I couldn't find any matching parts. Please try another keyword."
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
