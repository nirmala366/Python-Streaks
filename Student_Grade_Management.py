#initialize directory
#from ast import Delete


student_grades = {  }

#add new student
def add_student(name, grade):
    student_grades[name] = grade
    #[sagar] = 100
    print("Added {name} with a {grade}")
    #Added sagar with a 100

#update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        #sagar = 200
        print(f"{name} with marks are updated {grade}")

    else:
        print(f"{name} is not found!")

#delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been succesfully deleyed")

    else:
        print(f"{name} is not found!")

#view all students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")

    else:
        print("No students found/added")

#view a specific student
def main():
    while True:
        print('\n Student Grades Management System')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the programm...")
            break

        else:
            print("Invalid choice")
