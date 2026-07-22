
# Notice good use of functions for organized code!
def choose_option():
    print("1. View All Students")
    print("2. Add new Student")
    print("3. Search for student")
    print("4. Calculate grade stats")
    print("5. Exit ")
    usr = input("Enter an option (1-5): ")
    return usr

def view_students():
    print("ID | Name | Grade")
    file = open("students.txt", "r")

    lines = file.readlines()

    for line in lines:
        line = line.strip().split(",") # Use strip to remove newline
        print(f"ID: {line[0]} | Name: {line[1]} | Grade: {line[2]}")
    
    file.close() # good practice in case of memory leaks

def add_student():
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    # We want to make the ID the next id. For example if the last id was 1030, we want the new one to be 1031
    # Note this doesn't work if the students.txt file is empty
    
    file = open("students.txt", "r") # read first, to get last ID
    last_line = file.readlines()[-1].split(",")
    new_id = int(last_line[0])+1

    print(f"{name} with grade {grade} has been added, with ID {new_id}")
    file.close()

    file = open("students.txt", "a") # append now
    file.write(f"{new_id},{name},{grade}\n") # must add newline character
    file.close()

def search_student():
    found = False
    search_id = input("Enter ID to search: ")

    file = open("students.txt", "r")
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(",")
        if search_id == line[0]:
            print("Found student!")
            found = True
            print(f"{line[1]} has grade {line[2]}.")
            break
    
    if not found:
        print("Student not found.")
    
    file.close()

def grade_stats():
    grades = []
    student_count = 0
    # Lets use the other way to open a file
    with open("students.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            student_count += 1
            grade = int(line.strip().split(",")[2]) # because we only want the grade
            grades.append(grade)
    
    # because we used with, we don't have to cloes the file, it closes automatically when it exits the block

    print(f"Max: {max(grades)}")
    print(f"Min: {min(grades)}")
    print(f"Average: {sum(grades)/len(grades)}")
    print(f"Student count: {student_count}")

while True:

    option = choose_option()

    if option == "1":
        view_students()
    elif option == "2":
        add_student()
    elif option == "3":
        search_student()
    elif option == "4":
        grade_stats()
    elif option == "5":
        break
