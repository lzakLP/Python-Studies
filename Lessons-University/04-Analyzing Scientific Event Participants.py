# ACTIVITY: ANALYZING SCIENTIFIC EVENT PARTICIPANTS
#
# Develop a Python program that analyzes information about participants
# in a scientific event using sets, dictionaries, and NumPy arrays.
#
# The program must:
# 1. Store participant information in a list of dictionaries.
#    Each participant must have a name, location, affiliation,
#    and a list of areas of interest.
# 2. Use a set to identify the distinct regions participants come from.
# 3. Create a dictionary that groups participants' names by affiliation.
# 4. Store all participants' areas of interest in a NumPy array.
# 5. Use np.unique() with return_counts=True to count how many times
#    each area of interest appears.
# 6. Use np.argmax() to identify the most popular area of interest.
# 7. Display the regions, participants grouped by affiliation,
#    and the most popular area of interest.
#
# This activity practices sets, dictionaries, loops, comprehensions,
# and data analysis using NumPy.
#
# Write your code below:

# Import the required library.
import numpy as np

# Store participant information.
participants = [
    {
        "name": "Alice",
        "location": "USA",
        "affiliation": "University A",
        "interests": ["Physics", "Astronomy"],
    },
    {
        "name": "Bob",
        "location": "Brazil",
        "affiliation": "Institute B",
        "interests": ["Biology", "Astronomy"],
    },
    {
        "name": "Charlie",
        "location": "India",
        "affiliation": "Institute C",
        "interests": ["Chemistry", "Engineering"],
    },
    # Add more participants as needed.
]

# Use a set to identify distinct participant regions.
regions = {participant["location"] for participant in participants}

# Use a dictionary to group participants' names by affiliation.
affiliations = {}

for participant in participants:
    affiliation = participant["affiliation"]

    if affiliation not in affiliations:
        affiliations[affiliation] = []

    affiliations[affiliation].append(participant["name"])

# Create a NumPy array containing all areas of interest.
areas_of_interest = np.array([
    interest
    for participant in participants
    for interest in participant["interests"]
])

# Identify unique interests and count their occurrences.
unique_interests, counts = np.unique(
    areas_of_interest,
    return_counts=True,
)

# Find the area of interest with the highest count.
most_popular_area = unique_interests[np.argmax(counts)]

# Display the results. The order of regions in a set may vary.
print("Participant regions:", regions)

print("Participant affiliations:")
for affiliation, names in affiliations.items():
    print(f"{affiliation}: {', '.join(names)}")

print("Most popular area of interest:", most_popular_area)
