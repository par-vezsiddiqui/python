### least 5 rows. Read it back with DictReader and print only contacts whose name starts with a letter of your choice.

import csv

# Create contacts.csv
with open("contacts.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Phone"])
    writer.writeheader()

    writer.writerows([
        {"Name": "Aman", "Phone": "9876543210"},
        {"Name": "Rahul", "Phone": "9876543211"},
        {"Name": "Ankit", "Phone": "9876543212"},
        {"Name": "Priya", "Phone": "9876543213"},
        {"Name": "Ayesha", "Phone": "9876543214"}
    ])

# Read contacts.csv
with open("contacts.csv", "r") as file:
    reader = csv.DictReader(file)

    for contact in reader:
        if contact["Name"].startswith("A"):
            print(contact)