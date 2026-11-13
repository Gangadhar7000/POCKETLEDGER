from datetime import date, datetime
import csv
import io
import os
import sqlite3
from flask import Flask, Response, flash, redirect, render_template, request, url_for, abort

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, "expenses.db")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-this-key")

CATEGORIES = {
    "Expense": ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Education", "Other"],
    "Income": ["Salary", "Freelance", "Gift", "Investment", "Other"],
}

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount > 0),
                kind TEXT NOT NULL CHECK(kind IN ('Income', 'Expense')),
                category TEXT NOT NULL,
                transaction_date TEXT NOT NULL,
                note TEXT DEFAULT '',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

def valid_transaction(data):
    title = data.get("title", "").strip()
    kind = data.get("kind", "")
    category = data.get("category", "")
    amount_raw = data.get("amount", "").strip()
    tx_date = data.get("transaction_date", "")
    note = data.get("note", "").strip()

    errors = []
    try:
        amount = round(float(amount_raw), 2)
        if amount <= 0:
            errors.append("Amount must be greater than zero.")
    except (TypeError, ValueError):
        amount = 0
        errors.append("Enter a valid amount.")

    try:
        datetime.strptime(tx_date, "%Y-%m-%d")
    except (TypeError, ValueError):
        errors.append("Choose a valid transaction date.")

    if not title:
        errors.append("Description is required.")
    elif len(title) > 80:
        errors.append("Description must be 80 characters or fewer.")
    if kind not in CATEGORIES:
        errors.append("Choose Income or Expense.")
    elif category not in CATEGORIES[kind]:
        errors.append("Choose a valid category for the selected type.")
    if len(note) > 250:
        errors.append("Note must be 250 characters or fewer.")

    return {"title": title, "amount": amount, "kind": kind,
            "category": category, "transaction_date": tx_date, "note": note}, errors

@app.route("/")
def index():
    month = request.args.get("month", date.today().strftime("%Y-%m"))
    kind = request.args.get("kind", "All")
    search = request.args.get("q", "").strip()

    where = ["substr(transaction_date, 1, 7) = ?"]
    params = [month]
    if kind in ("Income", "Expense"):
        where.append("kind = ?")
        params.append(kind)
    if search:
        where.append("(title LIKE ? OR category LIKE ? OR note LIKE ?)")
        term = f"%{search}%"
        params.extend([term, term, term])

    clause = " AND ".join(where)
    with get_db() as conn:
        transactions = conn.execute(
            f"SELECT * FROM transactions WHERE {clause} ORDER BY transaction_date DESC, id DESC",
            params
        ).fetchall()
        totals = conn.execute("""
            SELECT
                COALESCE(SUM(CASE WHEN kind='Income' THEN amount ELSE 0 END), 0) AS income,
                COALESCE(SUM(CASE WHEN kind='Expense' THEN amount ELSE 0 END), 0) AS expense
            FROM transactions WHERE substr(transaction_date, 1, 7) = ?
        """, (month,)).fetchone()
        all_time = conn.execute("""
            SELECT
                COALESCE(SUM(CASE WHEN kind='Income' THEN amount ELSE 0 END), 0) AS income,
                COALESCE(SUM(CASE WHEN kind='Expense' THEN amount ELSE 0 END), 0) AS expense
            FROM transactions
        """).fetchone()

    return render_template(
        "index.html", transactions=transactions, month=month, kind=kind, search=search,
        income=totals["income"], expense=totals["expense"],
        balance=totals["income"] - totals["expense"],
        all_time_balance=all_time["income"] - all_time["expense"],
        today=date.today().isoformat(), categories=CATEGORIES
    )

@app.route("/add", methods=["POST"])
def add_transaction():
    data, errors = valid_transaction(request.form)
    if errors:
        for error in errors:
            flash(error, "error")
        return redirect(url_for("index"))
    with get_db() as conn:
        conn.execute("""
            INSERT INTO transactions (title, amount, kind, category, transaction_date, note)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (data["title"], data["amount"], data["kind"], data["category"],
              data["transaction_date"], data["note"]))
    flash("Transaction added successfully.", "success")
    return redirect(url_for("index", month=data["transaction_date"][:7]))

@app.route("/edit/<int:transaction_id>", methods=["POST"])
def edit_transaction(transaction_id):
    data, errors = valid_transaction(request.form)
    if errors:
        for error in errors:
            flash(error, "error")
        return redirect(url_for("index"))
    with get_db() as conn:
        result = conn.execute("""
            UPDATE transactions
            SET title=?, amount=?, kind=?, category=?, transaction_date=?, note=?
            WHERE id=?
        """, (data["title"], data["amount"], data["kind"], data["category"],
              data["transaction_date"], data["note"], transaction_id))
        if result.rowcount == 0:
            abort(404)
    flash("Transaction updated.", "success")
    return redirect(url_for("index", month=data["transaction_date"][:7]))

@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete_transaction(transaction_id):
    with get_db() as conn:
        result = conn.execute("DELETE FROM transactions WHERE id=?", (transaction_id,))
        if result.rowcount == 0:
            abort(404)
    flash("Transaction deleted.", "success")
    return redirect(url_for("index"))

@app.route("/export")
def export_csv():
    month = request.args.get("month", date.today().strftime("%Y-%m"))
    with get_db() as conn:
        rows = conn.execute("""
            SELECT transaction_date, title, kind, category, amount, note
            FROM transactions
            WHERE substr(transaction_date, 1, 7)=?
            ORDER BY transaction_date DESC, id DESC
        """, (month,)).fetchall()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Date", "Description", "Type", "Category", "Amount", "Note"])
    for row in rows:
        writer.writerow([row["transaction_date"], row["title"], row["kind"],
                         row["category"], f'{row["amount"]:.2f}', row["note"]])
    return Response(
        output.getvalue(), mimetype="text/csv",
        headers={"Content-Disposition": f"attachment; filename=transactions-{month}.csv"}
    )

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
