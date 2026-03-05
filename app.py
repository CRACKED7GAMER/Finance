import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Finance Advisor", layout="wide")

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ---------------- LOGIN FUNCTION ----------------
def login():
    if st.session_state.username == "admin" and st.session_state.password == "1234":
        st.session_state.logged_in = True
        st.session_state.page = "Dashboard"
        st.success("Login Successful")
        st.rerun()
    else:
        st.error("❌ Invalid Username or Password")

# ---------------- LOGOUT FUNCTION ----------------
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.password = ""
    st.rerun()

# ================= LOGIN PAGE =================
if not st.session_state.logged_in:

    st.title("💰 AI Personal Finance Advisor")

    st.markdown("### 🔐 Login to Continue")

    st.text_input("Username", key="username")
    st.text_input("Password", type="password", key="password")

    if st.button("Login"):
        login()

# ================= MAIN APP =================
else:

    # ---------------- SIDEBAR ----------------
    st.sidebar.title("📌 Navigation")

    page = st.sidebar.radio(
        "Go to",
        ["Dashboard", "Investments", "Loan Calculator"]
    )

    st.sidebar.markdown("---")
    st.sidebar.button("🚪 Logout", on_click=logout)

    # ================= DASHBOARD =================
    if page == "Dashboard":

        st.title("📊 Financial Dashboard")

        data = pd.DataFrame({
            "Category": ["Rent", "Food", "Transport", "Shopping", "Savings"],
            "Amount": [15000, 8000, 3000, 5000, 10000]
        })

        col1, col2 = st.columns(2)

        with col1:
            fig = px.pie(
                data,
                names="Category",
                values="Amount",
                hole=0.4,
                title="Expense Distribution"
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig2 = px.bar(
                data,
                x="Category",
                y="Amount",
                title="Monthly Spending"
            )
            st.plotly_chart(fig2, use_container_width=True)

    # ================= INVESTMENTS =================
    elif page == "Investments":

        st.title("📈 Investment Planner")

        amount = st.number_input("Investment Amount (₹)", min_value=0, value=10000)
        years = st.slider("Investment Years", 1, 30, 5)
        rate = st.slider("Expected Return (%)", 1, 20, 10)

        if st.button("Calculate Future Value"):

            future_value = amount * ((1 + rate / 100) ** years)

            st.success(f"💰 Future Value: ₹ {future_value:,.2f}")

    # ================= LOAN CALCULATOR =================
    elif page == "Loan Calculator":

        st.title("🏦 Loan EMI Calculator")

        loan_amount = st.number_input("Loan Amount (₹)", min_value=0, value=500000)
        interest_rate = st.slider("Interest Rate (%)", 1.0, 20.0, 8.0)
        tenure = st.slider("Loan Tenure (Years)", 1, 30, 10)

        if st.button("Calculate EMI"):

            monthly_rate = interest_rate / (12 * 100)
            months = tenure * 12

            emi = loan_amount * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

            st.success(f"📅 Monthly EMI: ₹ {emi:,.2f}")