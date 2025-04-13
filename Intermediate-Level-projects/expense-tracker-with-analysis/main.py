import json
import os
from datetime import datetime

class Expense:
    def __init__(self):
        self.datalist = []

    def time(self):
        date = datetime.now()
        time_now = date.strftime("%d %B, %Y %I:%M %p")
        return time_now

    @staticmethod
    def expense_menu():
        print("""
========= EXPENSE TRACKER =========
1. Add Expense
2. View Summary Report
3. View All Expenses
4. Exit
""")

    def add_expense(self, amount, category, desc):
        expense_dic = {
            "amount": amount,
            "category": category,
            "description": desc,
            "date": self.time()
        }
        self.datalist.append(expense_dic)

    def summary_reports(self):
        self.load_from_file()

        if self.datalist:
            summary = {}
            for items in self.datalist:
                category = items['category']
                amount = items['amount']

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

            print("\nExpense by Category:")
            for category, total in summary.items():
                print(f"- {category:8} : ৳{total}")

            most_expensive_category = max(summary, key=summary.get)
            print("\nMost expense on a category: ")
            print(f">>> {most_expensive_category}  : ৳{summary[most_expensive_category]}")
        else:
            print("\nNo data available\n")

    def view_all_expense(self):
        self.load_from_file()

        if self.datalist:
            print("Date                    | Category   | Amount  | Description")
            print("________________________|____________|_________|_____________")
            for item in self.datalist:
                print(f"{item['date']:<24} | {item['category']:<10} | {item['amount']:<7} | {item['description']:<30}")
            total_expense = sum(x['amount'] for x in self.datalist)
            print("________________________|____________|_________|_____________")
            print(f"          Total Expense: ৳{total_expense}")
        else:
            print("\nNo data available\n")

    def save_to_file(self):
        if os.path.exists("history.json"):
            with open("history.json", "r") as file:
                old_data = json.load(file)
        else:
            old_data = []

        old_data.extend(self.datalist)

        with open("history.json", "w") as file:
            json.dump(old_data, file, indent=4)

        self.datalist = []

    def load_from_file(self):
        if os.path.exists("history.json"):
            with open("history.json", "r") as file:
                self.datalist = json.load(file)
        else:
            self.datalist = []


def main():
    if not os.path.exists("history.json"):
        with open("history.json", "w") as file:
            json.dump([], file, indent=4)

    expense = Expense()
    is_running = True

    while is_running:
        expense.expense_menu()
        try:
            choose = int(input("Choose an option: "))

            if choose == 1:
                add_running = True
                while add_running:
                    while True:
                        try:
                            amount = int(input("Enter expense amount                      : ৳"))
                            break
                        except ValueError:
                            print("Please provide amount in number!")

                    category = input("Category (study/food/others)              : ").strip()
                    desc = input("For which reason? (Burger/Bus fare/others): ").strip()
                    expense.add_expense(amount, category, desc)

                    # Save to file
                    expense.save_to_file()

                    while True:
                        add_more = input("Want to add more expense? (y/n) : ").strip().lower()
                        if add_more == 'y':
                            break
                        elif add_more == 'n':
                            add_running = False
                            break
                        else:
                            print("INVALID INPUT!")

            elif choose == 2:
                expense.summary_reports()
            elif choose == 3:
                expense.view_all_expense()
            elif choose == 4:
                print("Exiting program...")
                is_running = False
            else:
                print("ONLY (1~4)")

        except KeyboardInterrupt:
            print("\nKeyboard Interrupt! Exiting...")
            is_running = False
        except ValueError:
            print("ONLY NUMBER! (1 ~ 4)")
        except Exception as err:
            print(f"Error happened: {err}")


if __name__ == "__main__":
    main()

