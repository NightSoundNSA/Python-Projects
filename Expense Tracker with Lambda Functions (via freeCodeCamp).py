# Expense Tracker with Lambda Functions

# Function to add an expense to the list
def add_expense(expenses, amount, category):
    # Appends a dictionary containing amount and category to the expenses list
    expenses.append({'amount': amount, 'category': category})
    
# Function to print all expenses
def print_expenses(expenses):
    for expense in expenses:
        # Iterates through the list and prints each expense
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
# Function to calculate total expenses
def total_expenses(expenses):
    # Uses lambda and map to extract amounts and sum them up
    return sum(map(lambda expense: expense['amount'], expenses))
    
# Function to filter expenses by category
def filter_expenses_by_category(expenses, category):
    # Uses lambda and filter to return expenses matching the given category
    return filter(lambda expense: expense['category'] == category, expenses)
    
# Main function to run the expense tracker application
def main():
    expenses = []  # Initialize an empty list to store expenses
    while True:
        # Display menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            # User inputs amount and category for a new expense
            amount = float(input('Enter amount: '))  # Convert input to float
            category = input('Enter category: ')
            add_expense(expenses, amount, category)  # Add expense to list

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)  # Display all recorded expenses
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))  # Show total cost
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)  # Show expenses in that category
    
        elif choice == '5':
            print('Exiting the program.')
            break  # Exit the loop and end the program

# Run the main function to start the program
main()

"""
Lesson Summary:
- **Lambda Functions:** Used for concise, anonymous functions to streamline operations.
- **map():** Used to extract and sum all amounts from expenses.
- **filter():** Used to retrieve expenses that match a specific category.
- **Function Design:** The program follows a modular design with separate functions for each operation.
- **User Interaction:** The program provides a simple menu for managing expenses.
"""
