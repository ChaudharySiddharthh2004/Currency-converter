
import streamlit as st

# ------------------ Page Configuration ------------------
st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱",
    layout="centered"
)

# ------------------ Custom CSS ------------------
st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

.title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#2E86C1;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:25px;
}

.box{
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0px 0px 12px rgba(0,0,0,0.15);
}

div.stButton > button{
    width:100%;
    background:#2E86C1;
    color:white;
    border:none;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

div.stButton > button:hover{
    background:#1B4F72;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ------------------ Title ------------------
st.markdown('<p class="title">💱 Currency Converter</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Convert currencies instantly</p>', unsafe_allow_html=True)

# ------------------ Exchange Rates ------------------
rates = {
    "USD 🇺🇸": 1,
    "INR 🇮🇳": 86,
    "EUR 🇪🇺": 0.85,
    "GBP 🇬🇧": 0.74,
    "JPY 🇯🇵": 148
}

# ------------------ Card ------------------
with st.container():

    amount = st.number_input(
        "💰 Enter Amount",
        min_value=0.0,
        value=1.0
    )

    col1, col2 = st.columns(2)

    with col1:
        from_currency = st.selectbox(
            "From",
            list(rates.keys())
        )

    with col2:
        to_currency = st.selectbox(
            "To",
            list(rates.keys()),
            index=1
        )

    st.write("")

    if st.button("🔄 Convert Currency"):

        usd = amount / rates[from_currency]

        result = usd * rates[to_currency]

        st.success(
            f"🎉 {amount:.2f} {from_currency} = {result:.2f} {to_currency}"
        )

        st.metric(
            label="Converted Amount",
            value=f"{result:.2f}"
        )

# ------------------ Footer ------------------
st.markdown("---")
st.caption("Made with ❤️ using Python & Streamlit")