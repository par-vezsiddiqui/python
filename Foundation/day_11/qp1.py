prices = {
    "apple": 20,
    "banana": 10,
    "milk": 50,
    "bread": 30,
    "eggs": 60
}

out_of_stock = {"banana", "eggs"}

orders = ["apple", "banana", "milk", "bread"]

total = 0

for item in orders:
    if item in out_of_stock:
        print(item, "is unavailable")
    else:
        total = total + prices[item]

print("Final order value:", total)