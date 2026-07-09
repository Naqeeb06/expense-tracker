# Creating an empty list
expenses_list = []


# function for adding expenses
def add_expense():
    print("Enter the expense details: \n")
    while(True):
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

    while(True):
            expense_category = input("Enter the category: \n")
            if not expense_category.strip():
                print("You cannot leave the field empty")
            else:
                break
    # creating a dictionary for storing a single expense
    expense_dict = {
        "Expense": expense,
        "Amount": expense_amount,
        "Category": expense_category,
    }
    expenses_list.append(expense_dict)

#function for displaying expenses
def display_expenses():
    if not expenses_list:
        print("No expenses added yet")
    else:
        print("Expense details: \n")
        for i, expense in enumerate(expenses_list):
            print(f"Expense # {i + 1}")
            print(f"\nExpense:{expense['Expense']}")
            print(f"Category:{expense['Category']}")
            print(f"Amount:{expense['Amount']}\n")


# Main menu
while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit" + "\n")

    user_input = input("Select an option (1-3): \n")

    # adding the expense
    if user_input == "1":
        while True:
            add_expense()
            # asking if user wants to add another expense
            choice = input(
                "Do you want to add another expense : \n Enter 'Y / y' for YES and 'N / n' for NO: "
            )
            if choice.lower() == "n":
                break

    # displaying the expense
    elif user_input == "2":
        display_expenses()

    # exiting the program
    elif user_input == "3":
        print("Till we meet again")
        break
    else:
        print("Invalid input. Please choose between 1 and 3")
