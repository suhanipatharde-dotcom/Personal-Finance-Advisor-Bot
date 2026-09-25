import os
from google import genai


def get_financial_advice(income, expenses, savings):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini AI is not configured yet. Please add GEMINI_API_KEY in your deployment environment."

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a personal finance advisor.

User financial information:
Monthly Income: ₹{income}
Total Expenses: ₹{expenses}
Current Savings: ₹{savings}

Provide:

1. A short summary of the user's financial situation.
2. Two practical ways to reduce unnecessary spending.
3. A suggested savings target.
4. One simple budgeting tip.

Keep the advice clear, practical and suitable for a normal individual.

Do not recommend specific stocks, securities, or investments.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text or "No advice was generated."

    except Exception as e:
        return f"Unable to generate AI advice: {str(e)}"
