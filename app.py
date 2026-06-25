import streamlit as st

st.set_page_config(
    page_title="PocketPilot AI",
    page_icon="💰",
    layout="centered"
)

st.title("💰 PocketPilot AI")
st.subheader("Financial Growth Coach for Teenagers")

st.markdown("---")

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

if st.button("Generate My Plan"):

    remaining = max(goal_amount - current_savings, 0)

    monthly_needed = remaining / months

    weekly_needed = monthly_needed / 4

    st.success("Your Financial Plan")

    st.markdown("### 🎯 Goal Summary")

    st.write(f"Goal: {goal_name}")
    st.write(f"Amount Needed: Rs. {remaining:,.0f}")

    st.markdown("### 📈 Savings Targets")

    st.metric(
        "Monthly Saving Needed",
        f"Rs. {monthly_needed:,.0f}"
    )

    st.metric(
        "Weekly Saving Needed",
        f"Rs. {weekly_needed:,.0f}"
    )

    st.markdown("### 💰 Suggested Budget")

    savings_budget = income * 0.30
    needs_budget = income * 0.50
    wants_budget = income * 0.20

    st.write(f"💵 Savings: Rs. {savings_budget:,.0f}")
    st.write(f"🏠 Needs: Rs. {needs_budget:,.0f}")
    st.write(f"🎮 Wants: Rs. {wants_budget:,.0f}")

    st.markdown("### 🧠 Financial Personality")

    ratio = monthly_needed / income if income > 0 else 0

    if ratio > 0.6:
        personality = "🎯 Goal-Oriented Saver"
    elif ratio > 0.3:
        personality = "⚖️ Balanced Planner"
    else:
        personality = "💸 Easy Spender"

    st.info(personality)

    st.markdown("### 🤖 PocketPilot Advice")

    if ratio > 0.6:
        st.write(
            "Your goal is ambitious. Focus on reducing unnecessary spending and prioritizing savings."
        )
    elif ratio > 0.3:
        st.write(
            "You have a realistic goal. Stay consistent and track your progress each week."
        )
    else:
        st.write(
            "You have room to improve your savings habits. Consider saving before spending."
        )

    st.balloons()
