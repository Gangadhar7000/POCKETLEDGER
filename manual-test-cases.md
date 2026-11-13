# Manual Test Cases

| ID | Test scenario | Steps / Input | Expected result |
|---|---|---|---|
| TC-01 | Open application | Run `python app.py`, visit localhost:5000 | Dashboard loads without errors |
| TC-02 | Add an expense | Enter title, positive amount, Expense, category and date | Expense appears in transaction list; monthly expense increases |
| TC-03 | Add income | Enter title, positive amount, Income, category and date | Income appears; monthly income and balance update |
| TC-04 | Reject empty description | Submit without a description | Validation message is displayed |
| TC-05 | Reject invalid amount | Enter zero, negative or non-numeric amount | Transaction is not saved |
| TC-06 | Filter by month | Select another month and apply filter | Only transactions for that month appear |
| TC-07 | Filter by type | Select Income or Expense | Only selected transaction type appears |
| TC-08 | Search transactions | Search for a known title or category | Matching records appear |
| TC-09 | Edit transaction | Click edit, change details and save | Updated details appear |
| TC-10 | Delete transaction | Click delete and confirm | Transaction is removed |
| TC-11 | Export CSV | Click Export CSV | A CSV file for the selected month downloads |
| TC-12 | Empty month | Select a month with no records | Empty-state message appears and totals show zero |
