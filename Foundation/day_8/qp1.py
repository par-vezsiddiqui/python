def calculate_library_fine(days_overdue, book_type='standard', is_premium_member=False):
    if days_overdue <= 0:
        return 0.0
    book_type = book_type.lower()
    if book_type == 'reference':
        fine = days_overdue * 20
    elif book_type == 'standard':
        if days_overdue <= 5:
            fine = days_overdue * 5
        else:
            fine = (5 * 5) + ((days_overdue - 5) * 10)
    else:
        raise ValueError("Invalid book type. Choose 'standard' or 'reference'.")
    if is_premium_member:
        fine *= 0.8  
    return fine

# print("1. Standard (3 days, regular):", calculate_library_fine(3)) 

# print("2. Standard (8 days, regular):", calculate_library_fine(8))

# print("3. Reference (4 days, regular):", calculate_library_fine(4, book_type='reference'))

# print("4. Standard (8 days, premium):", calculate_library_fine(8, is_premium_member=True))

# print("5. Reference (5 days, premium):", calculate_library_fine(5, book_type='reference', is_premium_member=True))