# QUESTION
# Develop a program that calculates the students' average grade,
# rounds the result to two decimal places, and determines the group's
# status based on that average.
#
# The program must:
# 1. Store the grades in a list.
# 2. Define a function to calculate the average using sum() and len().
# 3. Use a lambda function and round() to round the average.
# 4. Classify the group as "Passed" if the average is greater than or
#    equal to 7, or as "Failed" otherwise.
# 5. Display the grades, the rounded average, and the status.
#
# This activity practices functions defined with def, anonymous
# functions (lambda), Python's built-in functions, and conditional statements.
# The classification considers the group's average, not each individual grade.

# SOLUTION

# List of students' grades
grades = [7.5, 8.0, 6.5, 9.0, 7.0]

# Regular function to calculate the average
def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

# Lambda function to round the average to two decimal places
round_average = lambda average: round(average, 2)

# Calculate and round the average
average = calculate_average(grades)
rounded_average = round_average(average)

# Check the group's status based on the average
status = "Passed" if rounded_average >= 7 else "Failed"

# Display the results
print("Students' grades:", grades)
print("Rounded average:", rounded_average)
print("Status:", status)
