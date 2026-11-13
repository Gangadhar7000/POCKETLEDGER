# Use Cases — PocketLedger

## Primary actor
**User**

## Use cases
1. Add transaction
2. View monthly summary
3. View transaction history
4. Filter transactions
5. Search transactions
6. Edit transaction
7. Delete transaction
8. Export monthly transactions

## Use-case flow: Add transaction
1. User opens the dashboard.
2. User selects Income or Expense.
3. User enters description, amount, date and category.
4. User optionally enters a note.
5. User submits the form.
6. System validates the input.
7. System stores the transaction in SQLite.
8. System refreshes the dashboard and displays a success message.

## Use-case flow: Export transactions
1. User selects a month.
2. User clicks Export CSV.
3. System retrieves transactions for that month.
4. System generates and downloads a CSV file.
