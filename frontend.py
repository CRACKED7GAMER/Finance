import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Personal Finance Advisor", layout="wide")

# Sidebar
st.sidebar.title("💰 AI Finance Advisor")
st.sidebar.markdown("Manage your money smartly.")
st.sidebar.markdown("---")

st.sidebar.subheader("User Details")
income = st.sidebar.number_input("Monthly Income (₹)", min_value=0)
expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=0)
loan = st.sidebar.number_input("Monthly EMI (₹)", min_value=0)
goal = st.sidebar.text_input("Financial Goal")

# Main Page
st.title("📊 Personal Finance Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("💵 Income", f"₹{income}")
col2.metric("💳 Expenses", f"₹{expenses}")
col3.metric("🏦 EMI", f"₹{loan}")

savings = income - expenses - loan

st.markdown("---")

# Savings Highlight
if savings >= 0:
    st.success(f"💰 Monthly Savings: ₹{savings}")
else:
    st.error(f"⚠ You are overspending by ₹{abs(savings)}")

st.markdown("---")

# Pie Chart
if income > 0:
    labels = ['Expenses', 'EMI', 'Savings']
    values = [expenses, loan, max(savings, 0)]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    st.subheader("Expense Distribution")
    st.pyplot(fig)

st.markdown("---")

# Goal Section
st.subheader("🎯 Financial Goal")
if goal:
    st.info(f"Your Goal: {goal}")

st.markdown("---")

# Placeholder for AI Advice
st.subheader("🤖 AI Financial Advice")
st.write("AI suggestions will appear here after backend integration.")