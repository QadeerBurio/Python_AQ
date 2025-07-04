def bubble_sort_students(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j][1] > students[j + 1][1]:  # Compare marks
                students[j], students[j + 1] = students[j + 1], students[j]


def display_students(students):
    print("\n📋 Sorted Students by Marks:")
    for name, marks in students:
        print(f"{name} - {marks} marks")


def main():
    students = []
    n = int(input("How many students? "))

    for _ in range(n):
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        students.append((name, marks))

    print("\n🔄 Sorting students by marks using Bubble Sort...\n")
    bubble_sort_students(students)
    display_students(students)


if __name__ == "__main__":
    main()
