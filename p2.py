import json

class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        try:
            with open("transactions.json", "r") as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            pass

    def save_transactions(self):
        with open("transactions.json", "w") as file:
            json.dump(self.transactions, file)

    def add_income(self, amount, category):
        self.transactions.append({"type": "income", "amount": amount, "category": category})
        self.save_transactions()
        print("Income added successfully.")

    def add_expense(self, amount, category):
        self.transactions.append({"type": "expense", "amount": amount, "category": category})
        self.save_transactions()
        print("Expense added successfully.")

    def calculate_budget(self):
        total_income = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "income")
        total_expense = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "expense")
        remaining_budget = total_income - total_expense
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Remaining Budget: ${remaining_budget:.2f}")

    def expense_analysis(self):
        expense_categories = {}
        for transaction in self.transactions:
            if transaction["type"] == "expense":
                category = transaction["category"]
                amount = transaction["amount"]
                if category in expense_categories:
                    expense_categories[category] += amount
                else:
                    expense_categories[category] = amount
        print("Expense Analysis:")
        for category, amount in expense_categories.items():
            print(f"{category}: ${amount:.2f}")

def main():
    budget_tracker = BudgetTracker()
    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter the income amount: "))
            category = input("Enter the income category: ")
            budget_tracker.add_income(amount, category)
        elif choice == "2":
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            budget_tracker.add_expense(amount, category)
        elif choice == "3":
            budget_tracker.calculate_budget()
        elif choice == "4":
            budget_tracker.expense_analysis()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
