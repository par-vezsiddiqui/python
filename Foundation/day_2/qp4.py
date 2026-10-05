# 4. Monthly Allowance & Savings Planner

# Store monthly pocket money (float) and 3 expense variables (canteen, transport, shopping). Calculate remaining savings, check if is_budget_safe (bool), and print a summary.

# Monthly Allowance & Savings Planner

# Step 1: Store monthly pocket money and expenses
pocket_money = float(input("Enter monthly pocket money (₹): "))
canteen_expense = float(input("Enter canteen expenses (₹): "))
transport_expense = float(input("Enter transport expenses (₹): "))
shopping_expense = float(input("Enter shopping expenses (₹): "))

# Step 2: Calculate total expenses and remaining savings
total_expenses = canteen_expense + transport_expense + shopping_expense
remaining_savings = pocket_money - total_expenses

# Step 3: Check if the budget is safe (savings >= 0)
is_budget_safe = remaining_savings >= 0

# Step 4: Print the summary report
print("\n" + "=" * 35)
print("     MONTHLY SAVINGS PLANNER     ")
print("=" * 35)
print(f"Monthly Pocket Money : ₹{pocket_money:.2f}")
print("-" * 35)
print(f"Canteen Expense      : ₹{canteen_expense:.2f}")
print(f"Transport Expense    : ₹{transport_expense:.2f}")
print(f"Shopping Expense     : ₹{shopping_expense:.2f}")
print("-" * 35)
print(f"Total Expenses       : ₹{total_expenses:.2f}")
print(f"Remaining Savings    : ₹{remaining_savings:.2f}")
print(f"Is Budget Safe?      : {is_budget_safe}")
print("=" * 35)