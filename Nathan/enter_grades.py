students = [] # create an empty list to hold student names and scores
def letter_grade(score): # def function to determine letter grade
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def save_grades(filename="grades.csv"): # menu option 3. to save grades to a file
    global students
    with open(filename, "w") as f:
        for name, score in students: # traverse the list of students.
            grade = letter_grade(score)
            f.write(f"{name},{score},{grade}\n")

def read_grades(filename="grades.csv"): # menu option 4. to read grades from a file
    global students
    try:
        with open(filename, "r") as f:
            for line in f: # read each line from the file
                name, score, grade = line.strip().split(",") # read each line and split into components based on comma and create three variables nane, score, grade.
                print (name, score, grade)
                students.append((name, int(score)))
    except IOError:
        print ("file read error")
    students.sort(reverse=True)
    #print (students)
    return

# add a menu to this.  1. enter grades 2. show grades 3. save grades 4. read grades from file 9. quit
def enter_grades():
    another="y"
    # Input loop to collect student names and scores.  Menu 1.
    while another == "y":
        name = input("Enter your student name: ")
        score = int(input("Enter test score: "))
        grade ={"name":name, "score":score} # dictionary to hold name and score
        students.append(grade) # add the score object/dict to the students list
        another = input("Add another? (y/n): ")

def show_grades():
    totalscore = 0
    if len(students) == 0:
        print("no grades")
        return
    # Output loop to display each student's grade.  Menu 2.
    print ("Name.        Grade:")
    print ("===================")
    for name, score in students:
        #totalscore = 0
        grade = letter_grade(score)
        print(f"{name} : {score} : {grade}")
        totalscore += score

    average = totalscore/len(students)
    ct = len(students)
    print(f"Average grade: {letter_grade(average)} for {ct} students.")
    
    #students = read_grades()

def main_menu():
    choice = 0
    while choice != 9:
        print("\nMenu:")
        print("1. Enter Grades")
        print("2. Show Grades")
        print("3. Save Grades to File")
        print("4. Read Grades from File")
        print("9. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            enter_grades()
        elif choice == 2:
            show_grades()
        elif choice == 3:
            save_grades()
            print("Grades saved to grades.txt")
        elif choice == 4:
            #global students
            read_grades()
            print("Grades loaded from grades.txt")
        elif choice == 9:
            print("Exiting program.")
        else:
            print("Invalid choice. Please try again.")
def main():
    main_menu()

main()
