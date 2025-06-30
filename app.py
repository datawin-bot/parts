
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
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hi I am Parts Manager of Popular Auto Dealers. How can I help you."
    })

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask about a part number or description...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot reply
    with st.chat_message("assistant"):
        matches = []
        for idx, row in df.iterrows():
            part_no_score = fuzz.partial_ratio(prompt.lower(), str(row['Part No']).lower())
            desc_score = fuzz.partial_ratio(prompt.lower(), str(row['Part Desc']).lower())
            if max(part_no_score, desc_score) > 70:
                matches.append(row)

        if matches:
            result_df = pd.DataFrame(matches)
            reply = "Here are some matching parts:"
            st.markdown(reply)
            st.write(result_df)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        else:
            reply = "Sorry, I couldn't find any matching parts. Please try another keyword."
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

        closing = "Thanks for the enquiry, please share your Mobile number to get back to you."
        st.markdown(closing)
        st.session_state.messages.append({"role": "assistant", "content": closing})
