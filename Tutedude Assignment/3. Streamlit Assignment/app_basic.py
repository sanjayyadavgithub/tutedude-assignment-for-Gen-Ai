import streamlit as st
st.set_page_config(page_title="Home", layout="wide")

st.title("Welcome to Streamlit")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! from Input")
if st.button("Click me!"):
    st.success("Greet Me")
st.write(f"Greet Me button is clicked successfully! and Hello, {name}! from Input is displayed successfully!")
