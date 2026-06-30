import json
import os

FILE_NAME = "expenses.json"

# Load Data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save Data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add Income
def add_income():
    amount = float(input("Enter Income Amount: "))
    source = input("Enter Income Source: ")

    data = load_data()

    transaction = {
        "type": "Income",
        "amount": amount,
        "description": source
    }

    data.append(transaction)
    save_data(data)

    print("✅ Income Added Successfully!")

# Add Expense
def add_expense():
    amount = float(input("Enter Expense Amount: "))
    category = input("Enter Expense Category: ")

    data = load_data()

    transaction = {
        "type": "Expense",
        "amount": amount,
        "description": category
    }

    data.append(transaction)
    save_data(data)

    print("✅ Expense Added Successfully!")

# View Transactions
def view_transactions():
    data = load_data()

    if not data:
        print("No Transactions Found.")
        return

    print("\n===== TRANSACTION HISTORY =====")

    for item in data:
        print("--------------------------------")
        print("Type        :", item["type"])
        print("Amount      :", item["amount"])
        print("Description :", item["description"])

# View Balance
def view_balance():
    data = load_data()

    income = sum(item["amount"] for item in data if item["type"] == "Income")
    expense = sum(item["amount"] for item in data if item["type"] == "Expense")

    balance = income - expense

    print("\n===== FINANCIAL SUMMARY =====")
    print("Total Income  :", income)
    print("Total Expense :", expense)
    print("Balance       :", balance)

# Main Menu
while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        view_transactions()
    elif choice == "4":
        view_balance()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")


