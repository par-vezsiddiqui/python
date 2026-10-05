# FASTag Highway Toll Tax Calculator
# You are designing an automated toll plaza system on an Indian expressway. Write a program that evaluates toll rates using vehicle type, payment method, and festival status.
# Variables: vehicle_type (string), fastag_active (boolean), and is_national_holiday (boolean).

# Rules:
    # 1 - If FASTag is not active, print "Double toll penalty applied: cash mode".
    # 2 - If FASTag is active, check the holiday status:
    # If it is a national holiday, all vehicles get a 50 percent festive waiver. Print "Festive waiver applied: half toll".
    # If it is not a national holiday, charge standard rates: cars pay 100 rupees, SUVs pay 150 rupees, and trucks pay 300 rupees. Print the respective toll amount.
    # If an unrecognized vehicle type is passed, print "Invalid vehicle category".

# FASTag Highway Toll Tax Calculator

# Inputs
vehicle_type = input("Enter vehicle type (Car/SUV/Truck): ").strip().lower()
fastag_active = input("Is FASTag active? (yes/no): ").strip().lower() == "yes"
is_national_holiday = input("Is it a national holiday? (yes/no): ").strip().lower() == "yes"

# Standard toll rate lookup
toll_rates = {
    "car": 100,
    "suv": 150,
    "truck": 300
}

# Toll Logic
if not fastag_active:
    print("Double toll penalty applied: cash mode")
elif vehicle_type not in toll_rates:
    print("Invalid vehicle category")
elif is_national_holiday:
    standard_rate = toll_rates[vehicle_type]
    half_toll = standard_rate / 2
    print("Festive waiver applied: half toll")
    print(f"Toll Amount Payable: ₹{half_toll:.2f}")
else:
    standard_rate = toll_rates[vehicle_type]
    print(f"Standard Toll Amount Payable: ₹{standard_rate:.2f}")