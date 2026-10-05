# 2. Café Outing Split-Bill Calculator

# Build a cafe bill splitter for a hangout with friends. Take total bill amount and number of friends via input(). Cast inputs, add 10% tip, and print how much each person pays.


# Café Outing Split-Bill Calculator

# Step 1: Get total bill amount and number of friends via input() and cast them
total_bill = float(input("Enter total bill amount (₹): "))
num_friends = int(input("Enter number of friends: "))

# Step 2: Calculate 10% tip and final total with tip
tip_amount = total_bill * 0.10
grand_total = total_bill + tip_amount

# Step 3: Calculate share per person
per_person_share = grand_total / num_friends

# Step 4: Print summary report
print("\n" + "=" * 35)
print("     CAFÉ OUTING SPLIT-BILL     ")
print("=" * 35)
print(f"Base Bill Amount : ₹{total_bill:.2f}")
print(f"Tip (10%)        : ₹{tip_amount:.2f}")
print(f"Grand Total      : ₹{grand_total:.2f}")
print(f"Number of Friends: {num_friends}")
print("-" * 35)
print(f"Amount Per Person: ₹{per_person_share:.2f}")
print("=" * 35)