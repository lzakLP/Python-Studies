# Case Study: Building a Book Catalog
#
# Develop a basic library catalog using Python classes, lists, and Matplotlib.
#
# 1. Define a Book class with a title, author, and publication year.
#    Include a __str__ method to display each book's information.
# 2. Store Book objects in a list representing the library.
# 3. Create functions to add books and display the complete catalog.
# 4. Add the five sample books provided below.
# 5. Count the books published in each year, including repeated years.
# 6. Create a line chart with axis labels, a title, and numerical annotations.
#
# Requirement: Matplotlib must be installed.
# Run this command in your terminal if needed: pip install matplotlib
#
# Write your code below:

import matplotlib.pyplot as plt


# Define a class to represent a book.
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return (
            f"{self.title} by {self.author}, "
            f"published in {self.publication_year}"
        )


# Store the book objects in a list.
library = []


# Create a Book object and add it to the library.
def add_book(title, author, publication_year):
    new_book = Book(title, author, publication_year)
    library.append(new_book)
    print(f"The book '{title}' has been added to the library.")


# Display all books currently stored in the library.
def list_books():
    print("\nBooks in the Library:")

    if not library:
        print("The library is empty.")
        return

    for book in library:
        print(book)


# Add the sample books.
add_book("Don Quixote", "Miguel de Cervantes", 1605)
add_book("Pride and Prejudice", "Jane Austen", 1813)
add_book("1984", "George Orwell", 1949)
add_book("One Hundred Years of Solitude", "Gabriel García Márquez", 1967)
add_book("The Catcher in the Rye", "J. D. Salinger", 1951)

# Display the catalog.
list_books()

# Extract every publication year, preserving duplicates for accurate counting.
publication_years = [book.publication_year for book in library]

# Create a sorted list of distinct years for the horizontal axis.
years = sorted(set(publication_years))

# Count occurrences in the original list, which still contains duplicate years.
books_per_year = [publication_years.count(year) for year in years]

# Create the line chart.
plt.figure(figsize=(10, 5))
plt.plot(years, books_per_year, marker="o", linestyle="-")
plt.xlabel("Publication Year")
plt.ylabel("Number of Books")
plt.title("Books in the Library by Publication Year")

# Label each data point with its book count.
for year, count in zip(years, books_per_year):
    plt.annotate(
        str(count),
        (year, count),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center",
    )

# Use whole numbers for book counts and display each publication year.
plt.xticks(years, rotation=45)
plt.yticks(range(max(books_per_year) + 1))
plt.ylim(0, max(books_per_year) + 1)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Each sample year contains one book, so the chart displays a flat line at 1.
plt.show()
