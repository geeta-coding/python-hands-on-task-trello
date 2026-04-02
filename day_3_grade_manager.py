# this  is a grade manager 
student = {} # it stores a value and key pairs 

# creating a functions 
def add_student(name,grade):
    if name in student:
        print("student is already existing...")
    else:
        student[name] = grade
        print(f"{name} added ..")

def remove_student(name):
    if name in student:
        del student[name]
        print("removed....")
    else:
        print("stident is not found")

def average_grade(name):
    if name in student:
        grade = student[name]
        return sum(grade)/len(grade)
    else:
        print("student is not fount")

def class_status():
    all_state = []
    for grade in student.values():
        all_state.extend(grade)
    if not all_state:
        print("no data available")
        return
    average = 0
    high = max(all_state)
    low = min(all_state)
    av = sum(all_state)/len(all_state)

    print("class satatistic...\n")
    print("highest grade :",high)
    print("Low grade :  ",low)
    print("average : ",av)

def menu():
     

    while True:
        print("\n===== Grade Manager =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3.average grade")
        print("4. class status")
        print("5.exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            grades = list(map(int, input("Enter grades (space separated): ").split()))
            add_student(name, grades)

        elif choice == "2":
            name = input("Enter name: ")
            remove_student(name)

       

        elif choice == "3":
            name = input("Enter name: ")
            avg = average_grade(name)
            if avg is not None:
                print(f"📈 Average of {name}: {avg:.2f}")

       

        elif choice == "4":
            class_status()

        elif choice == "5":
            break

        else:
            print("invalid choice try again")

        


# ➤ Run Program
if __name__ == "__main__":
    menu()