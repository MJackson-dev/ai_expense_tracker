# AI Expense Tracker

AI-powered expense tracker that converts natural language inputs into structured financial data and automatically logs them into Google Sheets.

## 🚀 Overview

This project allows users to input expenses in plain language (e.g. "uber 10"), and automatically:

- Extracts structured data using AI
- Assigns payment based on user
- Generates the current date
- Sends the data to Google Sheets
- Calculates shared expenses and balances dynamically

---

## ⚙️ Features

- 🧠 Natural language expense parsing (OpenAI)
- 💸 Automatic expense splitting (handled in Google Sheets)
- 📅 Auto date generation (Python)
- 👤 User-based payment tracking
- ☁️ Google Sheets integration (gspread)
- 🔁 Fully automated workflow

---

## 🧱 Tech Stack

- Python
- OpenAI API (`gpt-4o-mini`)
- Google Sheets API (`gspread`)
- dotenv (environment variables)

---

## 🛠️ How It Works

1. User inputs an expense:
"Uber 10"
2. AI extracts:
```json
{
  "amount": 10000,
  "category": "transport",
  "description": "Uber"
}
```
- amount (numeric value, currency-agnostic)

3. Python:
- Adds current date
- Assigns who paid
4. Google Sheets handles:
- Expense splitting
- Balance calculation "Who owes who"

▶️ How to Run
1. Clone the repository
```
git clone https://github.com/YOUR_USERNAME/ai_expense_tracker.git
cd ai_expense_tracker
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Set up environment variables
- Create a .env file:
```
OPENAI_API_KEY=your_api_key_here
```
4. Add Google credentials
Create a service account
Download credentials.json
Share your Google Sheet with the service account email
5. Run the script _#Voice input in the near future#_
```
python main.py
```
6. Enter expense
```
Enter expense: Uber 10
```
📊 Example Output

Terminal:
```
User: martin
Martin paid: 10000
Loreto paid: 0
✅ Expense added to Google Sheets
```

Google Sheets:
-Automatically updates balances
-Calculates who owes who

🔮 Future Improvements

-CLI input (python main.py "uber 10 lucas")
-Telegram / WhatsApp integration
-Voice input
-Web or mobile interface
-Better category detection

🧠 Author

-Built by Martin as part of a journey into AI + automation + real-world systems.
