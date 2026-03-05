import streamlit as st

st.title("🏦 Loan Analyzer")

loan_amount = st.number_input("Loan Amount (₹)", 0)
interest = st.number_input("Interest Rate (%)", 0)
years = st.number_input("Loan Tenure (Years)", 0)

if st.button("Calculate EMI"):
    r = interest / 100 / 12
    n = years * 12
    emi = loan_amount * r * (1 + r)**n / ((1 + r)**n - 1)
    st.success(f"Monthly EMI: ₹{int(emi)}")