from crewai import Task
from crew_agents import style_analyzer, authorship_detector

style_analysis_task = Task(
    description="""
Analyze the writing style of the student based on these essays.

Essay 1:
{essay1}

Essay 2:
{essay2}

Essay 3:
{essay3}

Create a stylistic profile including:
- vocabulary patterns
- sentence length
- tone
""",
    agent=style_analyzer,
    expected_output="Detailed stylistic profile"
)

authorship_task = Task(
    description="""
Using the stylistic profile compare it with the following suspicious text.

{suspicious_text}

Determine if the same student likely wrote it.
Provide probability and explanation.
""",
    agent=authorship_detector,
    expected_output="Probability of authorship with reasoning"
)