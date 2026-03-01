from dotenv import load_dotenv
import os
import requests
import json
from .crew import build_crew
import re
import json

load_dotenv()

def send_to_telegram(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    print("DEBUG TOKEN:", token)
    print("DEBUG CHAT_ID:", chat_id)

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, data=payload)

    print("Telegram Status:", response.status_code)
    print("Telegram Response:", response.text)


def format_message(plan_json):
    return f"""
🍽 Tomorrow's Meal Plan

🥣 Breakfast:
{plan_json['breakfast']}

🍛 Lunch:
{plan_json['lunch']}

🍲 Dinner:
{plan_json['dinner']}

🔥 Calories: {plan_json['calories']}
💪 Protein: {plan_json['protein_g']}g
"""


if __name__ == "__main__":
    crew = build_crew()
    result = crew.kickoff()

    raw = result.raw

    match = re.search(r"\{.*\}", raw, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in LLM response")

    plan = json.loads(match.group())

    message = format_message(plan)
    send_to_telegram(message)

    print("Meal plan sent to Telegram 🚀")