import streamlit as st
import subprocess

def run_command(command):
    """Execute a shell command and return its output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

st.title("Autonomous Driving Deep RL Model Tester")

st.header("Test Model on Highway Environment")
if st.button("Test Model on Highway Environment"):
    st.write("Running command to test on HighwayEnv environment...")
    command = (
        "python experiments.py evaluate "
        ".\\configs\\HighwayEnv\\env.json "
        ".\\configs\\HighwayEnv\\agents\\DQNAgent\\dqn.json "
        "--recover --test --episodes=1 --verbose"
    )
    stdout, stderr = run_command(command)
    st.subheader("Output")
    st.text(stdout)
    # st.subheader("Error")
    # st.text(stderr)

st.header("Test Model on Intersection Environment")
if st.button("Test Model on Intersection Environment"):
    st.write("Running command to test on IntersectionEnv environment...")
    command = (
        "python experiments.py evaluate "
        ".\\configs\\IntersectionEnv\\env.json "
        ".\\configs\\IntersectionEnv\\agents\\DQNAgent\\ego_attention.json "
        "--recover --test --episodes=1 --verbose"
    )
    stdout, stderr = run_command(command)
    st.subheader("Standard Output")
    st.text(stdout)
    # st.subheader("Standard Error")
    # st.text(stderr)
