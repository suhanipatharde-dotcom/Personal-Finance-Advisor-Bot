import os
from google import genai


def get_financial_advice(income, expenses, savings):
    """Generate practical personal budgeting advice using Gemini."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return (
            "AI financial advice is not configured yet. "
            "Please configure the GEMINI_API_KEY environment variable."
        )

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
You are a personal budgeting assistant.

The user's recorded financial totals are:
Income: INR {income:.2f}
Expenses: INR {expenses:.2f}
Savings (income minus expenses): INR {savings:.2f}

Provide:
1. A short summary of the financial situation.
2. Two practical ways to manage unnecessary spending.
3. A realistic savings target based on the figures provided.
4. One simple budgeting tip.

Use clear, supportive language.
Do not recommend specific stocks, securities, or investments.
Do not claim that these totals represent a particular month
unless the user has provided that information.
Explain that this is general educational guidance, not
professional financial advice.
"""

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
            contents=prompt
        )

        advice = getattr(response, "text", None)

        if advice and advice.strip():
            return advice.strip()

        return "The AI advisor returned no advice. Please try again later."

    except Exception:
        # Avoid displaying API keys or raw internal errors to users.
        return (
            "Sorry, financial advice is temporarily unavailable. "
            "Please check your AI configuration and try again later."
        )

