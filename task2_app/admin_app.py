import streamlit as st
import pandas as pd

DATA_PATH = "data/reviews.csv"

st.title("Admin Feedback Dashboard")

df = pd.read_csv(DATA_PATH)

st.subheader("All User Submissions")
st.dataframe(df)

if not df.empty:
    st.subheader("Analytics")
    st.metric("Average Rating", round(df["rating"].mean(), 2))
    st.bar_chart(df["rating"].value_counts())
