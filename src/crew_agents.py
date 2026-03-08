import os
from crewai import Agent, Task, Crew, LLM
import os
from dotenv import load_dotenv

load_dotenv() 

API_KEY = os.getenv("CREWAI_API_KEY")  
my_llm = LLM(
    model="gemini/gemini-3-flash-preview",
    api_key=API_KEY
)

style_analyzer = Agent(
    role="Stylistic Analyzer",
    goal="Analyze the student's writing style from {essay1}, {essay2}, and {essay3}",
    backstory="Expert in linguistic analysis and authorship identification.",
    llm=my_llm,
    verbose=True
)

authorship_detector = Agent(
    role="Authorship Detector",
    goal="Compare the style of {suspicious_text} with the profile and determine probability",
    backstory="Specialist in academic integrity and plagiarism detection.",
    llm=my_llm,
    verbose=True
)

task1 = Task(
    description="Analyze the writing style of these three essays: {essay1}, {essay2}, {essay3}",
    expected_output="A detailed stylistic profile of the author.",
    agent=style_analyzer
)

task2 = Task(
    description="Compare the style of this text: {suspicious_text} with the created profile.",
    expected_output="Probability of authorship and explanation.",
    agent=authorship_detector
)

crew = Crew(
    agents=[style_analyzer, authorship_detector],
    tasks=[task1, task2],
    verbose=True
)
