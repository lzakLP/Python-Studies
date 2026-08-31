# Beecrowd 1020 - Age in Days
#
# Read a person's age in days and convert it into:
# - Years (365 days)
# - Months (30 days)
# - Remaining days
#
# The problem considers every year as 365 days
# and every month as 30 days.

age = int(input())

# Calculate the number of complete years
years = age // 365

# Calculate the remaining days after removing complete years
remaining_days = age % 365

# Calculate the number of complete months
months = remaining_days // 30

# Calculate the remaining days after removing complete months
days = remaining_days % 30

# Display the result
print(f"{years} year(s)")
print(f"{months} month(s)")
print(f"{days} day(s)")
