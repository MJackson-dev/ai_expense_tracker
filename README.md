# AI Expense Tracker

AI-powered expense tracker with **Telegram (text + voice) interface**, natural language understanding, and automatic logging to Google Sheets.

---

## 🚀 Overview

This project allows you to track expenses in the most natural way possible:

* Send a **text message** or **voice note** via Telegram
* AI extracts structured data (amount, category, description)
* Data is automatically logged into Google Sheets
* Expenses are split and balances calculated dynamically

👉 Example input:

* Text: `Almuerzo 8500`
* Voice: “Almuerzo doce mil”

---

## ⚙️ Features

* 🤖 **Telegram Bot Interface**

  * Text messages
  * Voice messages (`.ogg`, no conversion needed)

* 🧠 **AI-Powered Parsing**

  * Extracts:

    * amount
    * category
    * description
  * Handles Chilean context:

    * “lucas”
    * written numbers (“doce mil”)

* 🎤 **Speech-to-Text**

  * Uses OpenAI (`gpt-4o-mini-transcribe`)
  * Works directly with Telegram voice notes

* 📊 **Google Sheets Integration**

  * Automatic row insertion
  * Real-time expense tracking

* 💸 **Expense Splitting**

  * Handled via formulas in Google Sheets
  * Tracks who paid and who owes

* 🧱 **Clean Architecture**

  * Core function: `process_expense(text)`
  * Multiple input channels → one processing pipeline

---

## 🧱 Tech Stack

* Python
* OpenAI API

  * `gpt-4o-mini` (parsing)
  * `gpt-4o-mini-transcribe` (speech-to-text)
* Google Sheets API (`gspread`)
* python-telegram-bot
* dotenv

---

## 🛠️ How It Works

### 1. Input (Telegram or CLI)

```text
"Supermercado 15000"
"Almuerzo doce mil"
```

---

### 2. AI extracts structured data

```json
{
  "amount": 12000,
  "category": "food",
  "description": "almuerzo"
}
```

---

### 3. Python processing

* Assigns user (Martin / Loreto)
* Adds current date
* Prepares structured row

---

### 4. Google Sheets

Automatically:

* Stores data
* Splits expenses
* Calculates balances (“who owes who”)

---

## ▶️ How to Run

### 1. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/ai_expense_tracker.git
cd ai_expense_tracker
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

---

### 4. Google Sheets setup

* Create a service account
* Download `credentials.json`
* Share your Google Sheet with the service account email

---

### 5. Run the Telegram bot

```bash
python telegram_bot.py
```

Then in Telegram:

1. Search your bot
2. Click **Start**
3. Send a message or voice note

---

### (Optional) Run CLI version

```bash
python main.py
```

---

## 📊 Example Output

### Telegram

```
✅ Added: supermercado quince mil
```

---

### Google Sheets

* New row added automatically
* Balances updated in real time

---

## 🧭 Architecture

```text
Telegram (text / voice)
        ↓
transcribe_audio()   (if voice)
        ↓
process_expense(text)
        ↓
AI parsing (OpenAI)
        ↓
Google Sheets
```

---

## 🔮 Future Improvements

* Smarter confirmation messages (amount + category)
* Multi-user support (Telegram user detection)
* Weekly/monthly summaries
* WhatsApp integration
* Web/mobile interface
* Improved categorization

---

## 🧠 Author

Built by Martin as part of a journey into:

* AI systems
* Automation
* Real-world product building

---
