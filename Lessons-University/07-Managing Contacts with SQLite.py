# Exercise: Managing Contacts with SQLite
#
# Create a database named "contacts.db" and a table named "Contacts"
# to store contact names, email addresses, and phone numbers.
#
# Practice the four CRUD operations:
# 1. CREATE: Create the table and insert three sample contacts.
# 2. READ: Retrieve and display all contacts.
# 3. UPDATE: Change the second sample contact's phone number.
# 4. DELETE: Remove the first sample contact.
#
# Each contact must have an automatically generated ID.
# Use parameterized queries to supply values to SQL statements.
# Save your changes and close the database connection when finished.
#
# Requirement: sqlite3 is included in Python's standard library.
#
# Write your code below:

import sqlite3

# Connect to the database. SQLite creates the file if it does not exist.
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# CREATE: Create the Contacts table if it does not already exist.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT
    )
""")

# Define the sample contacts.
sample_contacts = [
    ("John", "john@example.com", "123-456-7890"),
    ("Mary", "mary@example.com", "987-654-3210"),
    ("Charles", "charles@example.com", "555-555-5555"),
]

# Insert the contacts and record their generated IDs.
# These IDs identify the correct records even if the database already exists.
contact_ids = []

for contact in sample_contacts:
    cursor.execute(
        "INSERT INTO Contacts (name, email, phone) VALUES (?, ?, ?)",
        contact,
    )
    contact_ids.append(cursor.lastrowid)

# Save the inserted records.
conn.commit()

# READ: Retrieve and display all contacts.
cursor.execute("SELECT id, name, email, phone FROM Contacts ORDER BY id")
contacts = cursor.fetchall()

print("Contacts:")
for contact in contacts:
    print(contact)

# UPDATE: Change the phone number of the second sample contact.
new_phone = "999-999-9999"
contact_id = contact_ids[1]

cursor.execute(
    "UPDATE Contacts SET phone = ? WHERE id = ?",
    (new_phone, contact_id),
)
conn.commit()

# DELETE: Remove the first sample contact.
contact_id_to_delete = contact_ids[0]

# The trailing comma creates a tuple containing a single parameter.
cursor.execute(
    "DELETE FROM Contacts WHERE id = ?",
    (contact_id_to_delete,),
)
conn.commit()

# Display the remaining contacts to verify the changes.
cursor.execute("SELECT id, name, email, phone FROM Contacts ORDER BY id")

print("\nContacts after the update and deletion:")
for contact in cursor.fetchall():
    print(contact)

# Close the database connection.
conn.close()
