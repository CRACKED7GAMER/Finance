import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Personal Finance Advisor", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.session_state.username == "admin" and st.session_state.password == "1234":
        st.session_state.logged_in = True
        st.rerun()
    else:
        st.error("Invalid Credentials")

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.title("💰 AI Personal Finance Advisor")
    st.subheader("Login")

    st.text_input("Username", key="username")
    st.text_input("Password", type="password", key="password")

    if st.button("Login"):
        login()

# ---------------- MAIN APP ----------------
else:

    st.sidebar.title("📌 Menu")
    page = st.sidebar.selectbox(
        "Navigate",
        ["Dashboard", "Investments", "Loan Calculator"]
    )

    if page == "Dashboard":
        st.title("📊 Dashboard")
        st.write("Welcome to your Dashboard 🎉")

    elif page == "Investments":
        st.title("📈 Investments Page")

    elif page == "Loan Calculator":
        st.title("🏦 Loan Calculator Page")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()