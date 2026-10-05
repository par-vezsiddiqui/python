# 2. Fibonacci Sequence

# Generate the first 10 numbers of the Fibonacci 

# Program to generate the first 10 Fibonacci numbers
n = 10
a, b = 0, 1

print("First 10 numbers of the Fibonacci sequence:")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()  # Newline for clean output