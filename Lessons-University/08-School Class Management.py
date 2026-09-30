# CASE STUDY: SCHOOL CLASS MANAGEMENT
#
# Develop a Python program to manage students and school classes.
# Each student has a name, a student ID, and grades for two subjects.
# Each class has a class number and can hold up to 30 students.
# Start with the five students and two classes provided below.
#
# Display a menu that allows the user to:
# 1. Enroll an existing student in a class.
# 2. Update a student's two grades.
# 3. Calculate the average of all grades in a selected class.
# 4. Display a class report with student names, IDs, and grades.
# 5. Exit the program.
#
# Validate input, prevent duplicate enrollment in the same class,
# and handle empty classes. Grade updates must appear in class reports.
# Assumption: grades range from 0 to 10.

from dataclasses import dataclass, field

SUBJECT_COUNT = 2
MAX_STUDENTS = 30


# These data classes replace the structures used in the C version.
@dataclass
class Student:
    name: str
    student_id: int
    grades: list[float]

    def average(self):
        return sum(self.grades) / len(self.grades)


@dataclass
class SchoolClass:
    class_number: int
    students: list[Student] = field(default_factory=list)


def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def read_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 10:
                return grade
        except ValueError:
            pass
        print("Invalid grade. Enter a number from 0 to 10 (example: 8.5).")


def choose_student(students):
    for student in students.values():
        print(f"{student.student_id} - {student.name}")
    student = students.get(read_integer("Student ID: "))
    if student is None:
        print("Student not found.")
    return student


def choose_class(classes):
    print("Available classes:", ", ".join(str(number) for number in classes))
    school_class = classes.get(read_integer("Class number: "))
    if school_class is None:
        print("Class not found.")
    return school_class


def main():
    # Dictionaries allow selection by student ID and class number.
    students = {
        1001: Student("João", 1001, [8.5, 7.0]),
        1002: Student("Maria", 1002, [7.5, 8.0]),
        1003: Student("Pedro", 1003, [9.0, 9.5]),
        1004: Student("Ana", 1004, [7.0, 7.5]),
        1005: Student("Carlos", 1005, [8.0, 8.5]),
    }
    classes = {5000: SchoolClass(5000), 6000: SchoolClass(6000)}

    # Repeat the menu until the user selects option 5.
    while True:
        print("\n1 - Enroll a student in a class")
        print("2 - Update a student's grades")
        print("3 - Calculate the class average")
        print("4 - Display a class report")
        print("5 - Exit")
        option = read_integer("Option: ")

        if option == 1:
            student = choose_student(students)
            if student is None:
                continue
            school_class = choose_class(classes)
            if school_class is None:
                continue

            if student in school_class.students:
                print("This student is already enrolled in this class.")
            elif len(school_class.students) >= MAX_STUDENTS:
                print("The class is full. No more students can be added.")
            else:
                # Store the same object so grade updates remain visible.
                school_class.students.append(student)
                print("Student enrolled successfully.")

        elif option == 2:
            student = choose_student(students)
            if student is None:
                continue
            student.grades = [
                read_grade(f"Grade for subject {i + 1}: ")
                for i in range(SUBJECT_COUNT)
            ]
            print("Grades updated successfully.")

        elif option == 3:
            school_class = choose_class(classes)
            if school_class is None:
                continue
            if not school_class.students:
                print("The class is empty. Its average cannot be calculated.")
                continue

            # Each student has two grades, so both averaging methods agree:
            # average all grades, or average the students' averages.
            average = sum(s.average() for s in school_class.students)
            average /= len(school_class.students)
            print(f"Class average: {average:.2f}")

        elif option == 4:
            school_class = choose_class(classes)
            if school_class is None:
                continue
            print(f"\nClass {school_class.class_number}")
            print(f"Total students: {len(school_class.students)}")
            if not school_class.students:
                print("No students are enrolled in this class.")
            for student in school_class.students:
                print(f"\nStudent: {student.name}")
                print(f"Student ID: {student.student_id}")
                print("Grades:", " ".join(f"{g:.2f}" for g in student.grades))
                print(f"Student average: {student.average():.2f}")

        elif option == 5:
            print("Program ended.")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
