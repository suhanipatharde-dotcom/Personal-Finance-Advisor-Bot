from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "finance.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT transaction_type, category, amount, description
        FROM transactions
        ORDER BY id DESC
    """)

    transactions = cursor.fetchall()

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM transactions
        WHERE transaction_type = 'income'
    """)
    income = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM transactions
        WHERE transaction_type = 'expense'
    """)
    expenses = cursor.fetchone()[0]

    savings = income - expenses

    conn.close()

    return render_template(
        "index.html",
        transactions=transactions,
        income=income,
        expenses=expenses,
        savings=savings
    )


@app.route("/add", methods=["POST"])
def add_transaction():
    transaction_type = request.form["transaction_type"]
    category = request.form["category"]
    amount = float(request.form["amount"])
    description = request.form["description"]

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (transaction_type, category, amount, description)
        VALUES (?, ?, ?, ?)
    """, (transaction_type, category, amount, description))

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM transactions WHERE id = ?",
        (transaction_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
