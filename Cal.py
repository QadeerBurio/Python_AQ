class GPACalculator:
    def __init__(self):
        self.students = []

    def calculate_gpa(self, grades, credits):
        total_points = 0
        total_credits = 0

        for grade, credit in zip(grades, credits):
            total_points += grade * credit
            total_credits += credit

        if total_credits == 0:
            return 0

        return round(total_points / total_credits, 2)

    def add_student(self):
        name = input("Enter student's name: ")
        grades_input = input("Enter grades (comma-separated): ")
        credits_input = input("Enter credit hours (comma-separated): ")

        try:
            grades = list(map(float, grades_input.split(',')))
            credits = list(map(float, credits_input.split(',')))

            if len(grades) != len(credits):
                print("Error: The number of grades and credits must be the same.")
                return

            gpa = self.calculate_gpa(grades, credits)
            self.students.append((name, gpa))
            print(f"{name}'s GPA is {gpa}")
        except ValueError:
            print("Error: Please enter valid numbers for grades and credit hours.")

    def show_history(self):
        if not self.students:
            print("No student records found.")
        else:
            print("\nGPA History:")
            for student in self.students:
                print(f"Name: {student[0]}, GPA: {student[1]}")

    def run(self):
        while True:
            print("\nGPA Calculator")
            print("1. Calculate GPA for a student")
            print("2. View GPA history")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.show_history()
            elif choice == '3':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    gpa_calculator = GPACalculator()
    gpa_calculator.run()
