from crewai import Crew
from crew_agents import style_analyzer, authorship_detector
from crew_tasks import style_analysis_task, authorship_task

crew = Crew(
    agents=[style_analyzer, authorship_detector],
    tasks=[style_analysis_task, authorship_task],
    verbose=True
)