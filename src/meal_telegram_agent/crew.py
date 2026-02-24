from crewai import Crew, Process
from .agents import meal_planner
from .tasks import meal_task

def build_crew():
    return Crew(
        agents=[meal_planner],
        tasks=[meal_task],
        process=Process.sequential
    )