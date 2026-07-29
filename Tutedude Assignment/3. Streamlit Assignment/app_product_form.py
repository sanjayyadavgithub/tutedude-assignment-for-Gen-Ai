import streamlit as st
st.set_page_config(page_title="Home", layout="wide")
st.title("Welcome to Product Form")
st.sidebar.header("Enter Product Details")
name = st.sidebar.text_input("Product Name")
price = st.sidebar.number_input("Price", min_value=0.0)
category = st.sidebar.selectbox(
    "Category",
    ["Electronics", "Clothing", "Food", "Other"]
)
submit = st.sidebar.button("Submit")
if submit:
    if name == "" or price == 0:
        st.warning("Please fill all details properly")
    else:
        st.success("Product Added Successfully!")
        st.subheader("Product Details")
        st.write(f"Name: {name}")
        st.write(f"Price: ₹{price}")
        st.write(f"Category: {category}")