import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(page_title="Simple Fitness Tracker", page_icon="🏋️", layout="centered")

# Title Section
st.title("🏋️ Simple Fitness Tracker")
st.markdown("""
Keep track of your workouts, monitor your progress, and view simple stats. Log your exercises and start your fitness journey today!
""")

# --- Workout Input ---
st.sidebar.header("➕ Add New Workout")
if "workouts" not in st.session_state:
    st.session_state.workouts = pd.DataFrame(columns=["Date", "Exercise", "Duration (minutes)", "Calories Burned"])

date = st.sidebar.date_input("Date", datetime.today())
exercise = st.sidebar.selectbox("Exercise", ["Running", "Cycling", "Yoga", "Strength Training", "Swimming", "Others"])
duration = st.sidebar.number_input("Duration (minutes)", min_value=1, max_value=600, step=1)
calories = st.sidebar.number_input("Calories Burned", min_value=0, max_value=2000, step=5)

if st.sidebar.button("Add Workout"):
    new_workout = pd.DataFrame({
        "Date": [date],
        "Exercise": [exercise],
        "Duration (minutes)": [duration],
        "Calories Burned": [calories]
    })
    st.session_state.workouts = pd.concat([st.session_state.workouts, new_workout], ignore_index=True)
    st.sidebar.success("Workout added!")

# --- Display Workouts ---
st.subheader("📋 Workout Summary")
st.dataframe(st.session_state.workouts, use_container_width=True)

# --- Fitness Statistics ---
if not st.session_state.workouts.empty:
    st.subheader("📊 Fitness Statistics")

    total_workouts = st.session_state.workouts.shape[0]
    total_duration = st.session_state.workouts["Duration (minutes)"].sum()
    total_calories = st.session_state.workouts["Calories Burned"].sum()

    st.write(f"Total Workouts Logged: {total_workouts}")
    st.write(f"Total Duration of Workouts: {total_duration} minutes")
    st.write(f"Total Calories Burned: {total_calories} kcal")

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ by a Beginner 💪")
