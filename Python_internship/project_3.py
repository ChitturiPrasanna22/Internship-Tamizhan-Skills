import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.json"

# ---------------- Load / Save Data ----------------
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

expenses = load_data()

# ---------------- Add Expense ----------------
def add_expense():
    category = input("Enter category (Food/Transport/Entertainment/Other): ")
    amount = float(input("Enter amount: "))
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ")

    if date_str == "":
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            date = date_str
        except ValueError:
            print("Invalid date format")
            return

    expenses.append({
        "category": category,
        "amount": amount,
        "date": date
    })

    save_data(expenses)
    print("Expense added successfully!")

# ---------------- Monthly Report ----------------
def monthly_report():
    month = input("Enter month (YYYY-MM): ")
    report = {}
    for item in expenses:
        if item["date"].startswith(month):
            cat = item["category"]
            report[cat] = report.get(cat, 0) + item["amount"]

    if not report:
        print("No expenses found for this month")
        return

    print(f"\nExpenses for {month}:")
    for cat, amt in report.items():
        print(f"{cat}: Rs. {amt}")

    return report

# ---------------- Plot Report ----------------
def plot_report(report):
    categories = list(report.keys())
    amounts = list(report.values())

    # Pie Chart
    plt.figure(figsize=(6,6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Monthly Expenses Distribution (Pie Chart)")
    plt.show()

    # Bar Chart
    plt.figure(figsize=(6,4))
    plt.bar(categories, amounts, color='skyblue')
    plt.title("Monthly Expenses Distribution (Bar Chart)")
    plt.xlabel("Category")
    plt.ylabel("Amount (Rs.)")
    plt.show()

# ---------------- View All Expenses ----------------
def view_expenses():
    if not expenses:
        print("No expenses recorded yet")
        return

    print("\nAll Expenses:")
    for item in expenses:
        print(f"{item['date']} | {item['category']} | Rs. {item['amount']}")

# ---------------- Main Menu ----------------
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Monthly Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        report = monthly_report()
        if report:
            plot_report(report)
    elif choice == "4":
        print("Exiting Expense Tracker")
        break
    else:
        print("Invalid choice")
