# You are writing ticket-booking logic for an IRCTC-style portal. Determine whether a passenger is eligible for a special senior citizen lower-berth preference and a ticket discount.

# The condition is met if the passenger is a senior citizen (age 60 or above) OR a female passenger traveling alone, AND they are booking a non-Tatkal ticket, but only if the journey is not on a blackout festival holiday date.

# IRCTC Ticket Booking Eligibility Logic

# Inputs
age = int(input("Enter passenger age: "))
gender = input("Enter gender (M/F/Other): ").strip().upper()
is_traveling_alone = input("Is the passenger traveling alone? (yes/no): ").strip().lower() == "yes"
is_tatkal = input("Is this a Tatkal booking? (yes/no): ").strip().lower() == "yes"
is_blackout_date = input("Is the journey on a blackout festival holiday date? (yes/no): ").strip().lower() == "yes"

# Condition Breakdown:
# 1. Senior citizen (age >= 60) OR female traveling alone
is_eligible_person = (age >= 60) or (gender == 'F' and is_traveling_alone)

# 2. Non-Tatkal ticket (not Tatkal)
is_non_tatkal = not is_tatkal

# 3. Not on a blackout festival holiday date
is_valid_date = not is_blackout_date

# Final Boolean evaluation using logical operators
is_eligible = is_eligible_person and is_non_tatkal and is_valid_date

# Output result
print("\n" + "=" * 45)
print("       IRCTC ELIGIBILITY CHECK RESULT       ")
print("=" * 45)
print(f"Eligible for Discount & Lower-Berth: {is_eligible}")
print("=" * 45)