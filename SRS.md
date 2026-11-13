# Software Requirements Specification (SRS)
## PocketLedger — Personal Expense Tracker

### 1. Introduction
PocketLedger is a small web-based application that helps an individual record and review personal income and expenses. It is intended as an educational Software Engineering mini-project.

### 2. Purpose
The purpose is to provide a simple interface for recording transactions, organising them into categories, reviewing monthly totals and exporting records.

### 3. Scope
The system supports manual transaction entry, monthly summaries, filtering, searching, editing, deletion and CSV export. It does not connect to banks or process payments.

### 4. User
- **User:** The person who records and manages their transactions.

### 5. Functional requirements
- FR-01: The system shall allow the user to add income and expense transactions.
- FR-02: The system shall validate required fields and positive amounts.
- FR-03: The system shall assign a category to each transaction.
- FR-04: The system shall display monthly income, expenses and balance.
- FR-05: The system shall filter transactions by month and type.
- FR-06: The system shall search transactions by title, category or note.
- FR-07: The system shall allow existing transactions to be edited or deleted.
- FR-08: The system shall export monthly transactions in CSV format.

### 6. Non-functional requirements
- NFR-01: The interface should be simple and responsive.
- NFR-02: Common actions should provide clear feedback.
- NFR-03: Transaction records should persist in an SQLite database.
- NFR-04: Inputs should be validated before database updates.
- NFR-05: The application should run on a typical computer with Python installed.

### 7. Hardware and software requirements
- Hardware: Computer with at least 2 GB RAM and a modern web browser.
- Software: Python 3.9+, Flask, SQLite and a modern browser.

### 8. Constraints
The application is designed for local educational use. It is not a substitute for a secure, audited financial product.
