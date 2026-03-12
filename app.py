import streamlit as st

def generate_plan(sport, goal, injury):
    plan = f"""
    Sport: {sport}
    Goal: {goal}
    Injury status: {injury}

    Example training session:
    1. Warm-up - 10 min
    2. Movement prep - 5 min
    3. Main block - sport-specific work
    4. Strength block - 3 exercises
    5. Cooldown - 5 min
    """
    return plan

st.title("Sportze.AI")
st.write("Generate a training session based on your sport and goal.")

sport = st.text_input("What sport do you play?")
goal = st.text_input("What is your goal?")
injury = st.text_input("Do you have any injury or limitation?")

if st.button("Generate training plan"):
    if sport and goal:
        result = generate_plan(sport, goal, injury)
        st.subheader("Your training plan")
        st.write(result)
    else:
        st.warning("Please fill in at least sport and goal.")
