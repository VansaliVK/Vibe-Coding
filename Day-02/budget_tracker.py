# Task 01: Ask for total monthly budget [cite: 97]
budget = float(input("Enter your total monthly budget: "))
total_expenses = 0

print("Enter your expenses (type 'done' when finished):")

# Task 03: Allow multiple entries until 'done' [cite: 104-107]
while True:
    user_input = input("Enter expense amount or 'done': ")
    
    if user_input.lower() == 'done':
        break
    
    try:
        expense = float(user_input)
        total_expenses += expense
    except ValueError:
        print("Please enter a valid number or 'done'.")

# Task 01: Subtract expenses and display balance [cite: 98-99]
balance = budget - total_expenses
print("-" * 20)
print(f"Total Budget: {budget}")
print(f"Total Expenses: {total_expenses}")
print(f"Remaining Balance: {balance}")

# Task 02: Low funds warning [cite: 100-103]
if balance < 500:
    print("Warning: Low Funds")
print("-" * 20)