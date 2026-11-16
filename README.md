# Python Studies

A collection of Python exercises developed while studying programming fundamentals, problem-solving, and software development concepts.

The repository brings together exercises from Beecrowd and university coursework. Each script is an independent solution and can be run separately.

## Topics covered

- Variables, input, output, and data types
- Arithmetic operations and basic algorithms
- Conditional statements and loops
- Lists, collections, and data processing
- Functions and modular problem-solving
- Object-oriented programming and inheritance
- Basic data modeling
- SQLite database operations

## Repository structure

```text
Python-Studies/
├── Lessons-Beecrowd/
│   ├── 01-Simple Calculate.py
│   ├── 02-Distance Between Two Points.py
│   ├── 03-Banknotes.py
│   ├── 04-Time Conversion.py
│   └── 05 - Age in Days.py
├── Lessons-University/
│   ├── 01-Discount Calculator.py
│   ├── 02-Average and Pass Status.py
│   ├── 03-Tracking Guest Confirmations.py
│   ├── 04-Analyzing Scientific Event Participants.py
│   ├── 05-Modeling Vehicle With Inheritance.py
│   ├── 06-Book Catalog.py
│   ├── 07-Managing Contacts with SQLite.py
│   ├── 08-School Class Management.py
│   ├── 09-Total Purchase Price.py
│   ├── 10-Bank Account Management.py
│   └── 11-Analyze the age of a Store's Custormers.py
└── README.md
```

## Requirements

- Python 3
- SQLite support for exercises that use the standard `sqlite3` module

No third-party packages are required by the exercises currently included in this repository.

## Run an exercise

Clone the repository:

```bash
git clone https://github.com/lzakLP/Python-Studies.git
cd Python-Studies
```

Run an individual script from the repository root. Use quotation marks because some filenames contain spaces:

```bash
python "Lessons-Beecrowd/01-Simple Calculate.py"
```

Another example:

```bash
python "Lessons-University/07-Managing Contacts with SQLite.py"
```

On Windows, the `py` launcher can be used instead:

```powershell
py "Lessons-Beecrowd/01-Simple Calculate.py"
```

## How to use this repository

1. Choose an exercise from one of the lesson directories.
2. Run the script with Python.
3. Provide the requested input in the terminal.
4. Review the output and the implementation.
5. Modify the solution to experiment with alternative approaches.

## Project scope

This is a study repository rather than a single installable application. Scripts are independent exercises, and there is currently no shared package, test suite, or application entry point.

The exercises are maintained as a record of learning and may evolve as new programming concepts are studied.
