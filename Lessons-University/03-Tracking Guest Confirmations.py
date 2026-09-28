# ACTIVITY: TRACKING GUEST CONFIRMATIONS
#
# Develop a Python program that identifies which guests have not yet
# confirmed their attendance at an event.
#
# The program must:
# 1. Store the guests' names in a tuple called guests.
# 2. Store the names of guests who have confirmed their attendance
#    in a list called confirmed_guests.
# 3. Use a list comprehension to create a list called unconfirmed_guests,
#    containing the guests who are not in confirmed_guests.
# 4. Display the names of the guests who have not yet confirmed,
#    one name per line.
# 5. Print a message about sending reminders to those guests.
#
# This activity practices tuples, lists, list comprehensions,
# the "not in" operator, and for loops.
# The program only displays a reminder message; it does not send messages.
#
# EXPECTED OUTPUT:
# Guests who have not yet confirmed:
# Alice
# Carol
# Eve
#
# Sending reminders to guests who have not yet confirmed.
#
# Write your code below:

# Store the guests' names in a tuple.
guests = ("Alice", "Bob", "Carol", "David", "Eve")

# Store the names of guests who have confirmed their attendance.
confirmed_guests = ["Bob", "David"]

# Identify guests who have not yet confirmed.
unconfirmed_guests = [
    guest for guest in guests if guest not in confirmed_guests
]

# Display each guest who has not yet confirmed.
print("Guests who have not yet confirmed:")

for guest in unconfirmed_guests:
    print(guest)

# Display a message about sending reminders.
print("\nSending reminders to guests who have not yet confirmed.")
