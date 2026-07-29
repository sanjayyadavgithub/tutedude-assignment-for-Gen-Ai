import streamlit as st
st.set_page_config(page_title="Home", layout="wide")
st.title("Welcome to Price Discount Calculator")
price = st.number_input("Enter the original price:")
discount_percentage = st.slider("Select discount percentage:", 1, 50, 10)
if st.button("Calculate Discounted Price"):
    discounted_price = price - (price * discount_percentage / 100)
    st.success(f"The discounted price is: {discounted_price:.2f}")
    st.write("### Price Details")
    st.write(f"Original Price: {price:.2f}")
    st.write(f"Discount Percentage: {discount_percentage}%")
    st.write(f"Discounted Price: {discounted_price:.2f}")
    st.write("### Price Comparison")
    table_data = [
            ["Before", price],
            ["After", discounted_price]
        ]
    st.table(table_data)



