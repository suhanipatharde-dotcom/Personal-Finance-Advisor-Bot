import os
import google.generativeai as genai


def get_financial_advice(income, expenses, savings):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini AI is not configured yet. Please add your Gemini API key."

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
You are a personal finance advisor.

User financial information:
Monthly Income: ₹{income}
Total Expenses: ₹{expenses}
Current Savings: ₹{savings}

Analyze this information and provide:
1. A short summary of the user's financial situation.
2. Two practical ways to reduce unnecessary spending.
3. A suggested savings target.
4. One simple budgeting tip.

Keep the advice clear, practical and suitable for a normal individual.
Do not recommend specific stocks, securities, or investments.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Unable to generate AI advice: {str(e)}"
