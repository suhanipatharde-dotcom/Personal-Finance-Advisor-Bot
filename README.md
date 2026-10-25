# Personal Finance Advisor Bot

## Project Overview
The Personal Finance Advisor Bot is a web-based application developed to help users track income and expenses, view savings, maintain transaction history, and receive AI-generated budgeting guidance.

## Objectives
- Record income and expense transactions.
- Calculate total income, expenses, and savings.
- Display transaction history.
- Provide personalised budgeting suggestions using AI.

## Technologies Used
- Python
- Flask
- SQLite
- HTML and CSS
- Google Gemini API
- Gunicorn
- Render for deployment

## Features
- Add income and expense transactions.
- Categorise transactions.
- View financial summaries.
- Review transaction history.
- Delete transactions.
- Request AI-generated financial guidance.

## Project Structure
- `app.py` — Flask application and transaction management.
- `ai_advisor.py` — AI financial advice generation.
- `requirements.txt` — Python dependencies.
- `templates/` — HTML templates for the web interface.

## Installation and Setup
1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Install dependencies:

   `pip install -r requirements.txt`

5. Configure the `GEMINI_API_KEY` environment variable if AI advice is required.
6. Run the application:

   `python app.py`

7. Open the local URL displayed by Flask in your browser.

## Deployment
The application is deployed using Render.

Live application: https://personal-finance-advisor-bot-pejk.onrender.com/

## Future Enhancements
- Monthly budgets and spending limits.
- Charts and expense analysis.
- Exportable financial reports.
- Improved transaction filtering.

## Disclaimer
This project provides general educational budgeting guidance and does not replace professional financial advice.
