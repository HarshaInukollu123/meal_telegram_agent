from crewai import Task
from .agents import meal_planner

meal_task = Task(
    description="""
Generate tomorrow's meal plan.

User:
28-year-old male
75kg
Goal: fat loss + muscle retention
Cuisine: South Indian
Budget: $75/week
Meals per day: 3
Cooking time: 45 min

Preferred Items:
 Breakfast
- Idli
- Dosa
- Pesarattu
- bread Avacado toast
- Upma
- ven pongal
- peanut chutney 

    lunch & dinner
- Chicken biryani / curry / fry / tandoori / butter chicken 
- Mutton curry / biryani
- Fish fry
- Sambar
- Rasam
- Curd rice
- spinach/Tomato /methi - dal 
- Egg curry , boiled, omlette
- Aloo
- Mushroom 
- okra 
- Tamarid rice
- veg pulao
- chapathi / chicken wrap / egg wrap 
- Mixed veg curry
- brinjal , ladiesfinger , cucumber
- prawns
- chana dal 
- salads 

Rules:
- Calories: 1800–1900
- Protein >= 130g
- Include fermented food
- 3 meals only
Return JSON only.
""",
    expected_output="""
A valid JSON object with:
{
  "breakfast": string,
  "lunch": string,
  "dinner": string,
  "calories": number,
  "protein_g": number
}
""",
    agent=meal_planner
)