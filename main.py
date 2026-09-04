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

        print("========== ADD INCOME ==========\n\n")

        try:

            amount = float(input("Enter Your Amount: "))
            category = input("Enter the Category: ")
            description = input("Enter the Description:")

            if amount<=0:
                print("Amount can't be in negetive nor zero")
                return

        except ValueError:
            print("Amount should be in numbers")
            return

        date = datetime.now().strftime("%Y-%m-%d")

        if not transactions:
            transaction_id = 1
        else:
            highest_id = 0
            for transaction in transactions:
                if transaction['id']>highest_id:
                    highest_id = transaction['id']

            transaction_id = highest_id + 1

        transaction = {'id': transaction_id, 'type':'Income', 'amount':amount,'category':category,'description':description,'date':date}

        transactions.append(transaction)

        self.save_transactions(transactions)

        print("Transaction Saved Succesfully")
        
    def add_expense(self):
        transactions = self.load_transactions()
        
        if transactions is None:
            return

        print("========== ADD EXPENSE ==========\n\n")

        try:

            amount = float(input("Enter Your Amount: "))
            category = input("Enter the Category: ")
            description = input("Enter the Description:")

            if amount<=0:
                print("Amount can't be in negetive nor zero")
                return

        except ValueError:
            print("Amount should be in numbers")
            return

        date = datetime.now().strftime("%Y-%m-%d")
        
        if not transactions:
            transaction_id = 1
        else:
            highest_id = 0
            for transaction in transactions:
                if transaction['id']>highest_id:
                    highest_id = transaction['id']

            transaction_id = highest_id + 1

        transaction = {'id': transaction_id, 'type':'Expense', 'amount':amount,'category':category,'description':description,'date':date}

        transactions.append(transaction)

        self.save_transactions(transactions)

        print("Transaction Saved Succesfully")
        
    def view_transactions(self):

        transactions = self.load_transactions()
        if transactions is None:
            return
        if not transactions:
            print("No Transactions Found")
            return

        print("========== ALL TRANSACTIONS ==========\n\n")

        for transaction in transactions:
            print(f"ID: {transaction['id']}")
            print(f"Type: {transaction['type']}")
            print(f"Amount: {transaction['amount']}")
            print(f"Category: {transaction['category']}")
            print(f"Description: {transaction['description']}")
            print(f"Date: {transaction['date']}")
            print("\n------------------------------\n")
            
    def search_transactions(self):
        transactions = self.load_transactions()
        if transactions is None:
            return
        if not transactions:
            print("No Transactions Found")
            return

        found = False

        print("========== SEARCH TRANSACTIONS ==========\n\n")
        print("1. Category")
        print("2. Date")
        print("3. Type")

        choice = input("\nEnter Your Choice: ")
        if choice =='1':
            search_category = input("\nSearch category: ").strip()
            print("\n\n========== SEARCH RESULTS ==========\n\n")
            for transaction in transactions:
                if transaction['category'].lower()==search_category.lower():
                    print(f"ID: {transaction['id']}")
                    print(f"Type: {transaction['type']}")
                    print(f"Amount: {transaction['amount']}")
                    print(f"Category: {transaction['category']}")
                    print(f"Description: {transaction['description']}")
                    print(f"Date: {transaction['date']}")
                    print("\n------------------------------\n")
                    found = True

            if found == False:
                print(f"No Transactions Found for Category: {search_category}")
        elif choice =='2':
            search_date = input("\nEnter Date (YYYY-MM-DD): ").strip()
            print("\n\n========== SEARCH RESULTS ==========\n\n")
            for transaction in transactions:
                if transaction['date']==search_date:
                    print(f"ID: {transaction['id']}")
                    print(f"Type: {transaction['type']}")
                    print(f"Amount: {transaction['amount']}")
                    print(f"Category: {transaction['category']}")
                    print(f"Description: {transaction['description']}")
                    print(f"Date: {transaction['date']}")
                    print("\n------------------------------\n")
                    found = True

            if found == False:
                print(f"No Transactions Found for Date: {search_date}")
        elif choice == '3':
            print("\n\n========== SEARCH BY TYPE ==========\n\n")
            print("1. Income")
            print("2. Expense")
            search_type = input("\nEnter your choice: ")

            if search_type == '1':
                print("\n\n========== SEARCH RESULTS ==========\n\n")
                for transaction in transactions:
                    if transaction['type'] == 'Income':
                        print(f"ID: {transaction['id']}")
                        print(f"Type: {transaction['type']}")
                        print(f"Amount: {transaction['amount']}")
                        print(f"Category: {transaction['category']}")
                        print(f"Description: {transaction['description']}")
                        print(f"Date: {transaction['date']}")
                        print("\n------------------------------\n")

                        found = True

                if found == False:
                    print("No income Transaction Found")

            elif search_type == '2':
                print("\n\n========== SEARCH RESULTS ==========\n\n")
                for transaction in transactions:
                    if transaction['type'] == 'Expense':
                        print(f"ID: {transaction['id']}")
                        print(f"Type: {transaction['type']}")
                        print(f"Amount: {transaction['amount']}")
                        print(f"Category: {transaction['category']}")
                        print(f"Description: {transaction['description']}")
                        print(f"Date: {transaction['date']}")
                        print("\n------------------------------\n")

                        found = True

                if found == False:
                    print("No expense Transaction Found")
            else :
                print("Invalid input")
        else:
            print("Invalid Input")

    def current_balance(self):
        transactions = self.load_transactions()
        if transactions is None:
            return
        if not transactions:
            print("No Transactions Found")
            return

        total_income = 0
        total_expense = 0

        for transaction in transactions:
            if transaction['type'] == 'Income':
                total_income += transaction['amount']
            else:
                total_expense += transaction['amount']

        balance = total_income - total_expense

        print("========== CURRENT BALANCE ==========\n\n")
        print(f"Total Income: {total_income}")
        print(f"Total Expense: {total_expense}")
        print(f"Current Balance: {balance}")
        
    def spending_by_category(self):
        transactions = self.load_transactions()
        if transactions is None:
            return
        if not transactions:
            print("No Transactions Found")
            return

        category_total = {}

        print("========== SPENDING BY CATEGORY ==========\n\n")

        for transaction in transactions:
            if transaction['type']== 'Expense':
                if transaction['category'] not in category_total:
                    category_total[transaction['category']] = transaction['amount']
                else:
                    category_total[transaction['category']] += transaction['amount']

        if not category_total:
            print("No Expense Transaction Found")
        else:
            for x in category_total:
                print(f"{x} :{category_total[x]}")
        
    def highest_expense(self):
        transactions = self.load_transactions()
        if transactions is None:
            return
        if not transactions:
            print("No Transactions Found")
            return

        highest_expense = None

        for transaction in transactions:
            if transaction['type'] == 'Expense':
                if highest_expense is None:
                    highest_expense = transaction
                else:
                    if highest_expense['amount']<transaction['amount']:
                        highest_expense = transaction

        print("========== HIGHEST EXPENSE ==========\n\n")
        if highest_expense is None:
            print("There is no Expense Transaction")
        else: 
            print(f"ID: {highest_expense['id']}")
            print(f"Type: {highest_expense['type']}")
            print(f"Amount: {highest_expense['amount']}")
            print(f"Category: {highest_expense['category']}")
            print(f"Description: {highest_expense['description']}")
            print(f"Date: {highest_expense['date']}")
            
    def monthly_summary(self):
        transactions = self.load_transactions()
        if transactions is None:
            return
        if not transactions:
            print("No Transactions Found")
            return

        print("========== MONTHLY SUMMARY ==========\n\n")

        try:
            search_year= int(input("Enter Year: "))
            search_month = int(input("Enter Month: "))
            if search_month<1 or search_month>12:
                print("Invalid Month!!!!")
                return
        except ValueError:
            print("Year/Month Should be in Number!!!")
            return

        total_income = 0
        total_expense = 0
        category_total = {}
        highest_expense = None
        found = False

        for transaction in transactions:
            date_parts = transaction['date'].split('-')
            year = int(date_parts[0])
            month = int(date_parts[1])
            if year ==search_year and month ==search_month:
                found = True
                if transaction['type'] =='Income':
                    total_income += transaction['amount']
                else:
                    total_expense += transaction['amount']
                    if transaction['category'] not in category_total:
                        category_total[transaction['category']] = transaction['amount']
                    else:
                        category_total[transaction['category']] += transaction['amount']

                    if highest_expense is None:
                        highest_expense = transaction
                    else:
                        if highest_expense['amount']<transaction['amount']:
                            highest_expense = transaction

        print("\n\n========== MONTHLY SUMMARY RESULT==========\n\n")
        if found == False:
            print("No Transaction Found")
        else:
            print(f"Year: {search_year}")
            print(f"Month: {search_month}")
            print("\n")
            print(f"Total Income: {total_income}")
            print(f"Total Expense: {total_expense}")
            print(f"Balance: {total_income - total_expense}")
            print("\n")
            print("Spending by Category:")
            if not category_total:
                print("No Expense Transaction Found")
            else:
                for x in category_total:
                    print(f"{x} :{category_total[x]}")

            print("\n")
            print("Highest Expense:")
            if highest_expense is None:
                print("There is no Expense Transaction")
            else: 
                print(f"ID: {highest_expense['id']}")
                print(f"Type: {highest_expense['type']}")
                print(f"Amount: {highest_expense['amount']}")
                print(f"Category: {highest_expense['category']}")
                print(f"Description: {highest_expense['description']}")
                print(f"Date: {highest_expense['date']}")
        
    def delete_transaction(self):
        transactions = self.load_transactions()
        if transactions is None:
            return
        if not transactions:
            print("No Transactions Found")
            return

        print("========== DELETE TRANSACTION ==========\n\n")
        try:
            
            search_id= int(input("Enter Transaction Id:"))
        except ValueError:
            print("Transaction Id Should Be A Number!")
            return

        for transaction in transactions:
            if transaction['id'] == search_id:
                transactions.remove(transaction)
                self.save_transactions(transactions)
                print("\nTransaction Deleted Successfully")
                return

        print("\nTransaction Not Found!")



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