# 1. Nested Loops: Prime Numbers

# Write a program to find and print all prime numbers between 2 and 50 using nested loops.

# Program to find prime numbers between 2 and 50 using nested loops

print("Prime numbers between 2 and 50:")

# Outer loop iterates through numbers from 2 to 50
for num in range(2, 51):
    is_prime = True  # Flag to track prime status
    
    # Inner loop checks for factors from 2 up to num - 1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # Found a factor, so it's not prime
            break            # Exit the inner loop early
            
    # If no factors were found, the number is prime
    if is_prime:
        print(num, end=" ")

print()  # Print a newline at the end