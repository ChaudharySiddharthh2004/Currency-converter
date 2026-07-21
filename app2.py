import streamlit as st

# Title
st.title("💱 Currency Converter")

# Exchange rates
rates = {
    "USD": 1,
    "INR": 86,
    "EUR": 0.85,
    "GBP": 0.74,
    "JPY": 148
}

# User Input
amount = st.number_input("Enter Amount", min_value=0.0)

from_currency = st.selectbox(
    "From Currency",
    list(rates.keys())
)

to_currency = st.selectbox(
    "To Currency",
    list(rates.keys())
)

# Button
if st.button("Convert"):

    usd_amount = amount / rates[from_currency]

    converted_amount = usd_amount * rates[to_currency]

    st.success(
        f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
    )
