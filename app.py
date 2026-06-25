import streamlit as st

st.set_page_config(
    page_title="PocketPilot AI",
    page_icon="💰",
    layout="centered"
)

st.title("💰 PocketPilot AI")
st.subheader("Personal Finance Coach for Teenagers")

income = st.number_input(
    "Monthly Income / Allowance (Rs.)",
    min_value=0
)

current_savings = st.number_input(
    "Current Savings (Rs.)",
    min_value=0
)

goal_name = st.text_input(
    "What are you saving for?"
)

goal_amount = st.number_input(
    "Goal Amount (Rs.)",
    min_value=1
)

months = st.number_input(
    "Goal Deadline (Months)",
    min_value=1
)

if st.button("Generate Plan"):

    remaining = goal_amount - current_savings

    monthly_needed = remaining / months

    weekly_needed = monthly_needed / 4

    st.success("Financial Plan Generated")

    st.write(f"### Goal: {goal_name}")

    st.write(
        f"Monthly Saving Needed: Rs. {monthly_needed:.0f}"
    )

    st.write(
        f"Weekly Saving Needed: Rs. {weekly_needed:.0f}"
    )
