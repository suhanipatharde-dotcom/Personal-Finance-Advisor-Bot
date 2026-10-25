
import os
import sqlite3
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for, flash
from ai_advisor import get_financial_advice

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key-change-before-production")

# Use a persistent database path when DATABASE_PATH is configured.
DATABASE = os.environ.get(
    "DATABASE_PATH",
    str(Path(__file__).resolve().parent / "finance.db")
)


def get_db_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DATABASE, timeout=10)
    return conn


def init_db():
    """Create the transactions table if it does not exist."""
    db_path = Path(DATABASE)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                transaction_type TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT
            )
        """)


def get_financial_summary():
    """Calculate total income, expenses, and savings."""
    with get_db_connection() as conn:
        income = conn.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM transactions
            WHERE transaction_type = 'income'
        """).fetchone()[0]

        expenses = conn.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM transactions
            WHERE transaction_type = 'expense'
        """).fetchone()[0]

    return income, expenses, income - expenses


@app.route("/")
def home():
    with get_db_connection() as conn:
        transactions = conn.execute("""
            SELECT id, transaction_type, category, amount, description
            FROM transactions
            ORDER BY id DESC
        """).fetchall()

    income, expenses, savings = get_financial_summary()

    return render_template(
        "index.html",
        transactions=transactions,
        income=income,
        expenses=expenses,
        savings=savings
    )


@app.route("/add", methods=["POST"])
def add_transaction():
    transaction_type = request.form.get(
        "transaction_type", ""
    ).strip().lower()
    category = request.form.get("category", "").strip()
    description = request.form.get("description", "").strip()
    amount_text = request.form.get("amount", "").strip()

    if transaction_type not in ("income", "expense"):
        flash("Please select a valid transaction type.")
        return redirect(url_for("home"))

    if not category:
        flash("Please enter a category.")
        return redirect(url_for("home"))

    try:
        amount = float(amount_text)
    except (ValueError, TypeError):
        flash("Please enter a valid amount.")
        return redirect(url_for("home"))

    if not (0 < amount < float("inf")):
        flash("Amount must be a positive, finite number.")
        return redirect(url_for("home"))

    with get_db_connection() as conn:
        conn.execute("""
            INSERT INTO transactions
            (transaction_type, category, amount, description)
            VALUES (?, ?, ?, ?)
        """, (transaction_type, category, amount, description))

    flash("Transaction added successfully.")
    return redirect(url_for("home"))


@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete_transaction(transaction_id):
    with get_db_connection() as conn:
        conn.execute(
            "DELETE FROM transactions WHERE id = ?",
            (transaction_id,)
        )

    flash("Transaction deleted.")
    return redirect(url_for("home"))


@app.route("/advice")
def advice():
    income, expenses, savings = get_financial_summary()

    financial_advice = get_financial_advice(
        income,
        expenses,
        savings
    )

    return render_template(
        "advice.html",
        advice=financial_advice,
        income=income,
        expenses=expenses,
        savings=savings
    )


# Initialize the database when the application starts.
init_db()


if __name__ == "__main__":
    app.run(debug=True)
