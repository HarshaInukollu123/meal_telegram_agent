from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2,
    api_key=os.getenv("OPENAI_API_KEY")
)

meal_planner = Agent(
    role="South Indian High-Protein Meal Planner",
    goal="Generate tomorrow's meal plan for fat loss and muscle retention",
    backstory="""
            You are a clinical nutrition AI.
            Cuisine: South Indian.
            Allowed proteins: eggs, chicken, fish, mutton.
            No beef or pork.
            Strictly follow calorie and protein targets.
            Return JSON only.
            """,
    llm=llm
)