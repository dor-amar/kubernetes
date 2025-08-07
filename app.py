students = []

def show_menu():
    """
    Displays the main menu with options for managing student data.
    """
    print("\n--- Student Management Menu ---")
    print("1. Add a Student")
    print("2. View All Students")
    print("3. Calculate Average Score")
    print("4. Find the Highest Scorer")
    print("5. Search for a Student")
    print("6. Update a Student")
    print("7. Delete a Student")
    print("8. Exit")

def add_student():
    """
    Prompts the user to input a student's name and score,
    validates the input, and adds the student to the students list.
    """
    name = input("Enter the student's name: ")
    while True:
        try:
            score = float(input("Enter the student's score (0-100): "))
            if 0 <= score <= 100:
                break
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    students.append({"name": name, "score": score})
    print(f"Student {name} with score {score} added successfully.")

def view_students():
    """
    Displays the list of all students with their names and scores.
    If no students are available, it notifies the user.
    """
    if not students:
        print("No students available.")
    else:
        print(f"{'Name':<20}{'Score':<10}")
        print("-" * 30)
        for student in students:
            print(f"{student['name']:<20}{student['score']:<10}")

def calculate_average():
    """
    Calculates and displays the average score of all students.
    If no students are available, it notifies the user.
    """
    if not students:
        print("No students available for calculating the average score.")
        return None
    total_score = sum(student['score'] for student in students)
    average_score = total_score / len(students)
    print(f"The average score of all the students is: {average_score:.2f}")

def find_highest_scorer():
    """
    Finds and displays the student with the highest score.
    Also displays a table of all students sorted by descending score.
    If no students are available, it notifies the user.

    Returns:
        dict: The student dictionary with the highest score, or None if no students exist.
    """
    if not students:
        print("No students available to find the highest scorer.")
        return None

    sorted_students = sorted(students, key=lambda student: student['score'], reverse=True)
    
    print("\nStudents sorted by score (highest to lowest):")
    print(f"{'Name':<20}{'Score':<10}")
    print("-" * 30)
    for student in sorted_students:
        print(f"{student['name']:<20}{student['score']:<10}")
    
    highest_scorer = sorted_students[0]
    print(f"\nThe highest scorer is {highest_scorer['name']} with a score of {highest_scorer['score']}.")
    return highest_scorer

def search_student():
    """
    Searches for a student by name and displays their details if found.
    """
    name = input("Enter the student's name to search: ")
    found = [s for s in students if s['name'].lower() == name.lower()]
    
    if found:
        print(f"{'Name':<20}{'Score':<10}")
        print("-" * 30)
        for student in found:
            print(f"{student['name']:<20}{student['score']:<10}")
    else:
        print(f"No student found with the name '{name}'.")

def update_student():
    """
    Updates a student's score based on their name.
    """
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student['name'].lower() == name.lower():
            try:
                new_score = float(input(f"Enter new score for {student['name']} (0-100): "))
                if 0 <= new_score <= 100:
                    student['score'] = new_score
                    print(f"{student['name']}'s score updated to {new_score}.")
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            return
    print(f"No student found with the name '{name}'.")

def delete_student():
    """
    Deletes a student from the list based on their name.
    """
    name = input("Enter the name of the student to delete: ")
    for i, student in enumerate(students):
        if student['name'].lower() == name.lower():
            confirm = input(f"Are you sure you want to delete {student['name']}? (y/n): ").lower()
            if confirm == 'y':
                students.pop(i)
                print(f"Student '{student['name']}' has been deleted.")
            else:
                print("Deletion cancelled.")
            return
    print(f"No student found with the name '{name}'.")

def main():
    """
    The main function that runs the interactive menu loop.
    Executes user-selected options until the user chooses to exit.
    """
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ")
        if choice == '1':
            print("Option 1 selected: Add a Student")
            add_student()
        elif choice == '2':
            print("Option 2 selected: View All Students")
            view_students()
        elif choice == '3':
            print("Option 3 selected: Calculate Average Score")
            calculate_average()
        elif choice == '4':
            print("Option 4 selected: Find the Highest Scorer")
            find_highest_scorer()
        elif choice == '5':
            print("Option 6 selected: Search for a Student")
            search_student()
        elif choice == '6':
            print("Option 7 selected: Update a Student")
            update_student()
        elif choice == '7':
            print("Option 8 selected: Delete a Student")
            delete_student()
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
