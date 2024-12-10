import streamlit as st
import pandas as pd
from utils.nlp_parser import parse_user_story
from utils.test_generator import generate_test_cases
from gpt_integration import generate_test_cases_with_gpt3
from utils.gherkin_generator import generate_gherkin_feature_file
import os
import re

# Set page configuration
st.set_page_config(
    page_title="Requirement Rebels - Test Case Generator",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add the logo on the left and team name with a tagline at the center
st.sidebar.image("assets/logo.png", width=150)

st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #4CAF50;">Requirement Rebels</h1>
        <h6>Challenging Limits, Defining Quality</h6>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if "test_cases" not in st.session_state:
    st.session_state["test_cases"] = []

# Option to select between single user story or file upload
st.subheader("Test Case Generation Options:")
generation_option = st.radio(
    "Select how you want to provide the user story:",
    options=["Single User Story", "Upload File with Multiple User Stories"]
)

# Checkbox for including negative scenarios
include_negative = st.checkbox("Include Negative Scenarios")

# Input for max test cases
max_cases = st.number_input("Max Number of Test Cases", min_value=1, max_value=10, value=3)

# Function to parse generated test case strings into structured dictionaries
def parse_gpt_test_case(case_str):
    """
    Parse the GPT-generated test case string into a structured dictionary.

    Args:
        case_str (str): The raw string of a generated test case.

    Returns:
        dict: A dictionary containing the parsed 'Steps' and 'Expected' keys.
    """
    # Initialize default values
    steps, expected = [], "No expected result defined"

    # Split the case string into lines
    lines = case_str.split("\n")

    # Regular expression to match step lines
    step_pattern = re.compile(r"^- step:", re.IGNORECASE)
    expected_pattern = re.compile(r"^- expected result:", re.IGNORECASE)

    for line in lines:
        line = line.strip()

        # Match "Step" lines with different possible cases
        if step_pattern.match(line):
            # Extract the step and add it to the list of steps
            steps.append(line.split(":", 1)[-1].strip())
        elif expected_pattern.match(line):
            # Extract the expected result
            expected = line.split(":", 1)[-1].strip()

    # If steps are not found, provide a meaningful fallback
    if not steps:
        steps = ["No steps defined."]

    return {"Steps": steps, "Expected": expected}

# Option 1: Single User Story Input
if generation_option == "Single User Story":
    user_story = st.text_area(
        "Enter a User Story:",
        placeholder="E.g., As a user, I want to reset my password so that I can access my account."
    )

    if st.button("Generate Basic Test Cases for Single User Story"):
        if user_story.strip():
            # Parse user story and generate basic test cases (non-LLM approach)
            parsed_data = parse_user_story(user_story)
            basic_cases = generate_test_cases(parsed_data, include_negative=include_negative)

            # Store basic test cases in session state
            st.session_state["basic_test_cases"] = basic_cases

            # Display generated basic test cases
            st.subheader("Generated Basic Test Cases:")
            for case in basic_cases:
                st.write(f"**Test Case {case['ID']}**")
                st.write(f"- **Step:** {case['Step']}")
                st.write(f"- **Expected:** {case['Expected']}\n")

    if st.button("Generate LLM Test Cases and Feature File for Single User Story"):
        if user_story.strip():
            # Generate GPT test cases with specified max_cases
            gpt_cases_raw = generate_test_cases_with_gpt3(user_story, max_cases, include_negative=include_negative)

            gpt_cases = [parse_gpt_test_case(case_str) for case_str in gpt_cases_raw[:max_cases]]

            # Store test cases in session state
            st.session_state["test_cases"] = [{
                "user_story": user_story,
                "gpt_cases": gpt_cases
            }]

            # Generate corresponding feature file for the user story using Gherkin format
            feature_filename = generate_gherkin_feature_file(user_story, gpt_cases)
            st.success("Feature file for the user story generated successfully.")

            # Display generated LLM test cases and feature file
            st.subheader("Generated LLM Test Cases:")
            for idx, case in enumerate(gpt_cases, 1):
                st.write(f"**Test Case {idx}**")
                st.write(f"- **Steps:**")
                if case['Steps']:
                    for step in case['Steps']:
                        st.write(f"  - {step}")
                else:
                    st.write("  - No steps defined.")
                st.write(f"- **Expected:** {case['Expected']}\n")

            # Provide option to download test cases as a text file
            test_cases_text = "\n".join(
                [f"Test Case {idx}:\n- Steps:\n" + "\n".join([f"  {step}" for step in case['Steps']]) + f"\n- Expected: {case['Expected']}\n"
                 for idx, case in enumerate(gpt_cases, 1)]
            )
            st.download_button(
                label="Download Test Cases",
                data=test_cases_text,
                file_name="generated_test_cases.txt",
                mime="text/plain"
            )

            st.subheader("Generated Feature File:")
            with open(feature_filename, "r") as file:
                st.text(file.read())

            # Provide option to download feature file
            with open(feature_filename, "r") as file:
                st.download_button(
                    label="Download Feature File",
                    data=file,
                    file_name=os.path.basename(feature_filename),
                    mime="text/plain"
                )
        else:
            st.error("Please enter a valid user story.")
