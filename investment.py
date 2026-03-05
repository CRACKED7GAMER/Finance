import streamlit as st

st.title("📈 Investment Planner")

sip = st.number_input("Monthly SIP Amount (₹)", 0)
rate = st.number_input("Expected Annual Return (%)", 0)
years = st.number_input("Investment Duration (Years)", 0)

if st.button("Calculate"):
    r = rate / 100 / 12
    n = years * 12
    future_value = sip * (((1 + r)**n - 1) / r)
    st.success(f"Estimated Future Value: ₹{int(future_value)}")