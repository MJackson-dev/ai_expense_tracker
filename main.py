CURRENT_USER = "martin"
CURRENT_USER = CURRENT_USER.lower()

from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()

from openai import OpenAI
import json

import gspread
from google.oauth2.service_account import Credentials

client = OpenAI()

def extract_expense(text):
    prompt = f"""
    Extract structured data from this expense:

    "{text}"

    Return JSON with:
    - amount (number, CLP)
    - category (food, transport, groceries, etc.)
    - description
    
    Chile context:
    - "lucas" = 1000 CLP

    Only return valid JSON. No extra text.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip().replace("```json", "").replace("```", "")

def append_to_sheet(row):
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "credentials.json", scopes=scope
    )

    client = gspread.authorize(creds)

    sheet = client.open("Expense_Tracker_Data").sheet1

    sheet.append_row(row)

text = input("Enter expense: ")

result = extract_expense(text)

print("\nRAW AI OUTPUT:")
print(result)

# Convert to Python dictionary

try:
    data = json.loads(result)
except json.JSONDecodeError:
    print("Error parsing AI response")
    print(result)
    exit()

print("\nPARSED DATA:")
print(data)

amount = data["amount"]

if CURRENT_USER == "martin":
    paid_martin = amount
    paid_loreto = 0
else:
    paid_martin = 0
    paid_loreto = amount

print("\nPAYMENT:")
print("User:", CURRENT_USER)
print("Martin paid:", paid_martin)
print("Loreto paid:", paid_loreto)

date = datetime.now().strftime("%Y-%m-%d")
description = data["description"]
category = data["category"]

row = [
    date,
    description,
    category,
    amount,
    paid_martin,
    paid_loreto
]

append_to_sheet(row)

print("\n✅ Expense added to Google Sheets")