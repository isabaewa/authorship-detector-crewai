import streamlit as st
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
    # Формируем входные данные только при нажатии кнопки
    inputs = {
        "essay1": essay1,
        "essay2": essay2,
        "essay3": essay3,
        "suspicious_text": suspicious_text
    }

    with st.spinner("Агенты работают..."):
        try:
            # Запуск внутри блока try, чтобы поймать ошибки API
            result = crew.kickoff(inputs=inputs)
            
            st.subheader("Result")
            st.write(result)
            
        except Exception as e:
            # Если возникнет проблема с ключом или регионом, вы увидите это здесь
            st.error(f"Произошла ошибка при работе CrewAI: {e}")
