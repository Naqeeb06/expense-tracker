import os
import csv

# ? function for adding expenses
def add_expense():
    print("Enter the expense details: \n")
    while True:
        expense = input("Enter the expense: \n")
        if not expense.strip():
            print("You cannot leave the field empty")
        else:
            break
    while True:
        try:
            expense_amount = int(input("Enter the amount: \n"))
            break
        except ValueError:
            print("\nEnter amount in numbers")

    while True:
        expense_category = input("Enter the category: \n")
        if not expense_category.strip():
            print("You cannot leave the field empty")
        else:
            break
    # ? creating a dictionary for storing a single expense
    expense_dict = {
        "Expense": expense,
        "Amount": expense_amount,
        "Category": expense_category,
    }

    save_expenses(expense_dict)


# ? function for displaying expenses
def display_expenses(expenses):
    if not expenses:
        print("No expense added yet")
        return
    print("=========================\nExpense details: \n=========================")
    for i, expense in enumerate(expenses):
        print(f"\n-------------------------\nExpense # {i + 1} \n-------------------------")
        print(f"Expense:{expense['Expense']}")
        print(f"Category:{expense['Category']}")
        print(f"Amount:{expense['Amount']}")


# ? function for saving expenses to csv file
def save_expenses(expense):
    file_exists = os.path.exists("expenses.csv")
    with open("expenses.csv", "a", newline="") as csvfile:
        field_names = ["Expense", "Amount", "Category"]
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        if not file_exists:
            writer.writeheader()
        writer.writerow(expense)


# ? function for loading expenses from csv file
def load_expenses():
    expenses = []
    file_exists = os.path.exists("expenses.csv")
    if not file_exists:
        return expenses
    
    with open("expenses.csv", "r", newline="") as read_file:
        reader = csv.DictReader(read_file)

        for row in reader:
            row["Amount"] = int(row["Amount"])
            expenses.append(row)
    return expenses

#? function for calculating the total expense
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["Amount"]
    return total

#? function for deleting an expense
def delete_expense():
    expenses = load_expenses()
    if not expenses:
        print("No expenses available to delete\n")
        return
    #!displaying the expenses to user so he can choose which one to delete
    display_expenses(expenses)

    #!asking the user to choose the expense number
    while True:
        try:
            user_choice = int(input("Choose the expense you want to delete.Enter the number:  "))
            if user_choice > len(expenses) or user_choice < 1:
                print("Invalid expense number")
            else:
                break
        except ValueError:
            print("Kindly enter the expense number.")
        
    
    index = user_choice - 1
    deleted_expense = expenses.pop(index)
    save_all_expenses(expenses)
    print("Deleted successfully\n")
    print(f"Expense: {deleted_expense['Expense']}")
    print(f"Amount: {deleted_expense['Amount']}")
    print(f"Category: {deleted_expense['Category']}\n")



#? function for saving all expenses
def save_all_expenses(expenses):
    with open("expenses.csv", 'w', newline="") as csvfile:
        field_names = ["Expense", "Amount", "Category"]
        writer = csv.DictWriter(csvfile, fieldnames= field_names)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

#?function containing the main menu
def main_menu():
    print("\n====================\nExpense Tracker\n====================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit" + "\n")

# Main menu
while True:
    main_menu()
    user_input = input("Select an option (1-5): \n")

    #! adding the expense
    if user_input == "1":
        while True:
            add_expense()
            # asking if user wants to add another expense
            choice = input(
                "Do you want to add another expense : \n Enter 'Y / y' for YES and 'N / n' for NO: "
            )
            if choice.lower() == "n":
                break

    #! displaying the expense
    elif user_input == "2":
        expenses = load_expenses()
        display_expenses(expenses)

    #!calculating total expense
    elif user_input == "3":
        expenses = load_expenses()
        if not expenses:
            print("No expense added yet")
        else:
            total = calculate_total(expenses)
            print("\nTotal Expense = " , total, "\n")
    
    #!deleting an expense
    elif user_input == "4":
        delete_expense()

    #! exiting the program
    elif user_input == "5":
        print("Till we meet again")
        break
    else:
        print("Invalid input. Please choose between 1 and 5")
