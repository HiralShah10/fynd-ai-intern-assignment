import streamlit as st
import pandas as pd
import json
import os

DATA_PATH = "data/reviews.csv"

st.title("Customer Feedback")

rating = st.selectbox("Select Rating", [1, 2, 3, 4, 5])
review = st.text_area("Write your review")

def call_llm_user(review, rating):
    return {
        "response": "Thank you for your feedback! We value your experience.",
        "summary": "User shared feedback about their experience.",
        "action": "Monitor feedback and respond if needed."
    }

if st.button("Submit"):
    ai_output = call_llm_user(review, rating)

    new_row = {
        "rating": rating,
        "review": review,
        "ai_response": ai_output["response"],
        "ai_summary": ai_output["summary"],
        "recommended_action": ai_output["action"]
    }

    df = pd.read_csv(DATA_PATH)
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)

    st.success(ai_output["response"])
