print("STUDENT GRADE CALCULATOR")

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter mark for Subject {i}: "))
    marks.append(mark)

if any(mark < 0 or mark > 100 for mark in marks):
    print("Invalid marks! Enter marks between 0 and 100.")
else:
    total = sum(marks)
    average = total / 5

    print("\nStudent Name:", name)
    print("Total Marks:", total, "/ 500")
    print("Average:", average)

    if any(mark < 35 for mark in marks):
        print("Result: FAIL")
        print("Grade: F")
    elif average >= 90:
        print("Result: PASS")
        print("Grade: A+")
    elif average >= 75:
        print("Result: PASS")
        print("Grade: A")
    elif average >= 60:
        print("Result: PASS")
        print("Grade: B")
    else:
        print("Result: PASS")
        print("Grade: C")
