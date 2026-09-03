import json 
from datetime import datetime

class ExpenseTracker:
    def load_transactions(self):

        try:
            with open('transactions.json','r') as file:
                transactions = json.load(file)
            return transactions
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("sorry json file is currepted")
            return None


    def save_transactions(self, transactions):
        with open("transactions.json",'w') as file:
            json.dump(transactions,file,indent=4)


    def add_income(self):
        transactions = self.load_transactions()

        if transactions is None:
            return

        amount = int(input("Enter Your Amount: "))
        


        pass
    def add_expense(self):
        pass
    def view_transactions(self):
        pass
    def search_transactions(self):
        pass
    def current_balance(self):
        pass
    def spending_by_category(self):
        pass
    def highest_expense(self):
        pass
    def monthly_summary(self):
        pass
    def delete_transaction(self):
        pass


def main():
    system = ExpenseTracker()
    while True:

        
        print("\n\n========== PERSONAL EXPENSE TRACKER ==========\n\n")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. Search Transactions")
        print("5. View Current Balance")
        print("6. View Spending by Category")
        print("7. Show Highest Expense")
        print("8. Monthly Summary")
        print("9. Delete Transaction")
        print("10. Exit")

        choice = input("\nEnter your Choice: ")
        print("\n")
        if choice == '1':
            system.add_income()
        elif choice =='2':
            system.add_expense()
        elif choice == '3':
            system.view_transactions()
        elif choice =='4':
            system.search_transactions()
        elif choice =='5':
            system.current_balance()
        elif choice =='6':
            system.spending_by_category()
        elif choice == '7':
            system.highest_expense()
        elif choice == '8':
            system.monthly_summary()
        elif choice =='9':
            system.delete_transaction()
        elif choice =='10':
            print("Thank you!!")
            break
        else:
            print("Invalid Input, Select 1 - 10")

if __name__ == "__main__":
    main()