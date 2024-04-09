import os
import json

def load_expenses():
    if os.path.exists('expenses.json'):
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    else:
        expenses = {}
    return expenses

def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)

def add_expense(expenses, category, amount):
    if category not in expenses:
        expenses[category] = []
    expenses[category].append(amount)

def generate_report(expenses):
    total_expenses = 0
    print("Expense Report:")
    for category, amounts in expenses.items():
        category_total = sum(amounts)
        total_expenses += category_total
        print(f"{category}: ${category_total}")
    print(f"Total Expenses: ${total_expenses}")

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Generate Expense Report")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, category, amount)
            save_expenses(expenses)
            print("Expense added successfully!")
        elif choice == '2':
            generate_report(expenses)
        elif choice == '3':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
