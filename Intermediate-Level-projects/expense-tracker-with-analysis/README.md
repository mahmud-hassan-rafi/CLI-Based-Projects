# Expense Tracker using Python and JSON

This is a terminal-based **Expense Tracker** built using **Python**. It allows users to keep track of their daily expenses, view reports by category, and store all data in a JSON file (`history.json`) for persistence.

---

## Features

- Add expenses with amount, category, and description  
- View total expenses by category  
- See all historical expenses with timestamp  
- Identify the category with the highest total expense  
- Automatically saves and loads from `history.json`  

---

## Technologies Used

- Python standard libraries: `json`, `os`, `datetime`

---

## Getting Started

### Requirements

- Python 3.x

### How to Run

1. Clone this repository or copy the code to a file named `expense_tracker.py`
2. Open terminal and run:

```bash
python expense_tracker.py
```

---

## Menu Options

```
========= EXPENSE TRACKER =========
1. Add Expense
2. View Summary Report
3. View All Expenses
4. Exit
```

---

## Sample Output

### Adding an Expense

```
Enter expense amount                      : ৳100
Category (study/food/others)              : food
For which reason? (Burger/Bus fare/others): Burger
Want to add more expense? (y/n) : y
```

### Viewing Summary Report

```
Expense by Category:
- food     : ৳320
- study    : ৳150

Most expense on a category: 
>>> food  : ৳320
```

### Viewing All Expenses

```
Date                    | Category   | Amount  | Description
________________________|____________|_________|_____________
05 June, 2025 09:42 AM  | food       | 120     | Burger                        
05 June, 2025 09:45 AM  | study      | 150     | Book Purchase                 
________________________|____________|_________|_____________
          Total Expense: ৳270
```

---

## File Details

- `main.py`: Main Python script
- `history.json`: Auto-created JSON file that stores all expenses

---

## How It Works

- All expenses are temporarily stored in `self.datalist` and saved to `history.json`
- When the program starts or displays reports, it loads from this JSON file
- Each entry includes amount, category, description, and timestamp
- Reports are generated based on aggregated data from this file

---

## Improvements You Can Add

- Export summary report to CSV or Excel
- Monthly filters
- GUI interface using Tkinter or PyQt
- Password protection

---

## License

This project is free to use for learning and personal use.
