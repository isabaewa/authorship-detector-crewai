import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(__file__))

from crew_setup import crew

st.title("Diploma Authorship Detector")

st.header("Agent Configuration")

analyzer_role = st.text_input(
    "Analyzer Role",
    "Stylistic Analyzer"
)

detector_role = st.text_input(
    "Detector Role",
    "Authorship Detector"
)

st.header("Input Data")

essay1 = st.text_area("Essay 1")
essay2 = st.text_area("Essay 2")
essay3 = st.text_area("Essay 3")

suspicious_text = st.text_area("Suspicious Diploma Chapter")

st.header("Run Analysis")

if st.button("Start Crew"):

    inputs = {
        "essay1": essay1,
        "essay2": essay2,
        "essay3": essay3,
        "suspicious_text": suspicious_text
    }

    result = crew.kickoff(inputs=inputs)

    st.subheader("Result")

    st.write(result)