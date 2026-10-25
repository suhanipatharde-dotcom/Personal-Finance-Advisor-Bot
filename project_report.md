# Personal Finance Advisor Bot

## 1. Project Overview

The Personal Finance Advisor Bot is a web-based application designed to help users record their income and expenses, monitor their savings, and receive AI-generated financial guidance. The application provides a simple interface for managing transactions and understanding spending habits.

## 2. Problem Statement

Many individuals find it difficult to track daily expenses, control unnecessary spending, and maintain a regular savings plan. Manual record-keeping can be inconvenient and does not always provide useful insights. This project aims to provide a simple digital solution for recording financial transactions and generating personalized budgeting suggestions.

## 3. Objectives

- Develop a user-friendly personal finance management web application.
- Allow users to add and delete financial transactions.
- Store transaction information in an SQLite database.
- Display income, expenses, and savings summaries.
- Integrate Google's Gemini AI to generate general financial guidance.
- Encourage responsible spending and regular saving habits.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web application framework |
| SQLite | Transaction data storage |
| HTML and CSS | User interface |
| Google Gemini API | AI-generated financial guidance |
| Gunicorn | Production application server |
| Render | Web application deployment |
| GitHub | Source code and version control |

## 5. System Features

### 5.1 Dashboard
Displays the financial summary and recorded transactions.

### 5.2 Transaction Management
Allows users to record financial transactions and delete existing entries.

### 5.3 Financial Summary
Calculates and displays income, expenses, and savings based on the application's implemented logic.

### 5.4 AI Financial Advice
Uses the Gemini API to generate general budgeting guidance, spending-reduction suggestions, and savings recommendations based on the financial summary.

### 5.5 Database
Uses SQLite to store transaction records for retrieval by the application.

## 6. System Architecture

The application follows a simple web architecture:

1. The user interacts with the website through a browser.
2. The HTML templates display the dashboard and financial advice pages.
3. The Flask application processes requests and performs calculations.
4. SQLite stores and retrieves transaction data.
5. The AI advisor module sends a financial summary to the Gemini API when advice is requested.
6. The generated advice is displayed on the website.

## 7. Project File Structure

```text
Personal-Finance-Advisor-Bot/
├── app.py
├── ai_advisor.py
├── requirements.txt
├── README.md
├── project_report.md
└── templates/
    ├── index.html
    └── advice.html
```

## 8. Implementation

The main application is implemented in `app.py` using Flask. It handles web routes, transaction operations, database access, and financial summaries.

The `ai_advisor.py` module manages the Gemini API integration and returns financial guidance. The `templates/index.html` file provides the main dashboard, while `templates/advice.html` displays AI-generated advice.

The `requirements.txt` file lists the Python packages needed to run the application. The application is deployed using Render, and its source code is maintained in GitHub.

## 9. Testing

The following checks should be performed and their actual results recorded before final submission.

| Test case | Expected result |
|---|---|
| Open the application | Dashboard loads successfully |
| Add a transaction | Transaction is saved and displayed |
| Delete a transaction | Selected transaction is removed |
| View financial summary | Summary reflects recorded transactions |
| Request AI advice with API configured | Financial guidance is displayed |
| Request AI advice when the API is unavailable | A user-friendly error message is displayed |
| Restart or reload the application | Stored transactions remain available when persistent storage is configured correctly |

## 10. Security and Limitations

- The Gemini API key should be stored as an environment variable and must not be committed to GitHub.
- A production secret key should be configured through the deployment environment.
- The application provides general educational budgeting guidance and is not a substitute for professional financial advice.
- AI-generated suggestions may not always be accurate.
- The current application is a student project and may require additional authentication, privacy controls, and testing before use with sensitive real-world financial information.

## 11. Future Scope

- Add user registration and secure login.
- Introduce monthly budgets and spending categories.
- Add charts showing expense trends.
- Provide downloadable financial reports.
- Improve input validation and automated testing.
- Add stronger privacy and security controls.

## 12. Conclusion

The Personal Finance Advisor Bot demonstrates how Python, Flask, SQLite, and generative AI can be combined to build a personal finance management application. It supports transaction tracking, financial summaries, and AI-generated budgeting guidance. The project provides a foundation for further improvements in financial awareness and expense management.

## 13. Project Links

- **GitHub repository:** https://github.com/suhanipatharde-dotcom/Personal-Finance-Advisor-Bot
- **Live application:** https://personal-finance-advisor-bot-pejk.onrender.com/

---

**Note:** Testing results should be updated to match the tests actually performed. Do not include passwords or API keys in this report or repository.
