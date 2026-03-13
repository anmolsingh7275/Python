import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("KPI Data Analysis Dashboard")

# Load sample data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 18000, 17000, 21000, 24000],
    "Customers": [200, 240, 260, 250, 300, 320]
}

df = pd.DataFrame(data)

# Show dataset
st.subheader("Dataset")
st.write(df)

# KPI Metrics
st.subheader("Key Performance Indicators")

total_sales = df["Sales"].sum()
avg_sales = df["Sales"].mean()
total_customers = df["Customers"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales}")
col2.metric("Average Monthly Sales", f"${avg_sales:.0f}")
col3.metric("Total Customers", total_customers)

# Sales Trend Chart
st.subheader("Monthly Sales Trend")

fig, ax = plt.subplots()
ax.plot(df["Month"], df["Sales"], marker="o")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.set_title("Sales Trend")

st.pyplot(fig)

# Customer Trend
st.subheader("Customer Growth")

fig2, ax2 = plt.subplots()
ax2.bar(df["Month"], df["Customers"])
ax2.set_xlabel("Month")
ax2.set_ylabel("Customers")

st.pyplot(fig2)