# PocketLedger — Personal Expense Tracker

A responsive personal finance web app built with **Python Flask, SQLite, HTML, CSS and JavaScript**. Track income and expenses, review your monthly balance, search transactions, edit or delete entries, and export monthly records to CSV.

## Features

- Add income and expense transactions
- Categorise transactions with type-specific categories
- Monthly income, expense and balance summaries
- Filter by month and transaction type
- Search by description, category or note
- Edit and delete transactions
- Export a month's transactions as CSV
- Responsive layout for desktop and mobile
- SQLite database is created automatically on first run

## Requirements

- Python 3.9 or newer
- pip

## Run locally

### 1. Download or clone this repository

```bash
git clone https://github.com/YOUR-USERNAME/pocketledger.git
cd pocketledger
```

### 2. Create and activate a virtual environment

Windows:

```bash
py -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser. The SQLite database (`expenses.db`) is created automatically in the project folder.

## Project structure

```text
pocketledger/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   ├── app.js
│   └── style.css
└── tests/
    └── manual-test-cases.md
```

## Manual test cases

See [`tests/manual-test-cases.md`](tests/manual-test-cases.md).

## Software Engineering documentation

Suggested deliverables for the mini-project report:

1. Problem statement and objectives
2. Software Requirements Specification (SRS)
3. Use case diagram
4. Data Flow Diagram (DFD)
5. Entity Relationship Diagram (ERD)
6. Test plan and test results
7. Screenshots of the running application

## Database

The `transactions` table stores:

| Field | Description |
|---|---|
| id | Unique transaction ID |
| title | Transaction description |
| amount | Positive amount |
| kind | Income or Expense |
| category | Transaction category |
| transaction_date | Date in YYYY-MM-DD format |
| note | Optional note |
| created_at | Record creation timestamp |

## Notes

- This is a local educational project, not a production financial service.
- No bank account or payment credentials are collected.
- The default Flask secret key is for local development only. Set the `SECRET_KEY` environment variable before any deployment.
- The database file is excluded from Git using `.gitignore`; each user gets a fresh local database.

## License

This project is available for educational and personal use.
