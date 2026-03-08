from crewai import Agent

style_analyzer = Agent(
    role="Stylistic Analyzer",
    goal="Analyze the student's writing style from previous essays",
    backstory="Expert in linguistic analysis and authorship identification.",
    verbose=True
)

authorship_detector = Agent(
    role="Authorship Detector",
    goal="Compare writing style and determine authorship probability",
    backstory="Specialist in academic integrity and plagiarism detection.",
    verbose=True
)