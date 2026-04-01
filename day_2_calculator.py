import math 

history = []
memory = 0

# creating a function for claculation

def calculation (a,b,operator):
    if operator == '+':
        return a+b
    elif operator =='-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '%':
        return a%b
    else :
        raise ValueError("Invalid operator for calculation.....")

# creating a menu driven

def show_menu():
    print("\n============ SMART CALCULATOR ==========")
    print("\n1.basic calculator")
    print("\n 2.scientific calculator")
    print("\n 3.Meomory number for recalling6" \
    "")
    print("\n 4.memory recall")
    print("\n 5.show history")
    print("\n 6.exist..")


def basic_cal():
    try:
        a = float(input("enter the number 1: "))
        b = float(input("enter the number 2:"))
        operator = input("enter the correct operator(+ , - ,*, %)")

        result = calculation(a,b,operator)
        print("the result : ",result)
        history.append(f"{a} {operator} {b} = {result}")
    except ValueError as v:
        print("error",v)
    except ZeroDivisionError as d :
        print("error",d)
    except Exception:
        print("invalid input")

def scientific_calculator():
    try :
        num = float(input("enter the number "))

        print("sin : ",math.sin(num))
        print("cos",math.cos(num))

        if num < 0:
            print("squar root not defined for the negative numbers...")
        else :
            print("squre root : ",math.sqrt(num))
    except ValueError:
        print("please enter the valid number")

def memory_store():
    global memory
    try:
        memory = float(input("enter the number for store"))
        print("stored successfully......\n")
    except ValueError:
        print("invalid memory.....")

def memory_recall():
    print("memory value : ",memory)


def show_history ():
    if not history:
        print("no history yet....")
    else :
        print("calculation history...\n")

        for i in history:
            print(i,"\n")

def main():
    while True:
        show_menu()
        choice = input("enter your choice...")

        if choice =='1':
            basic_cal()
        elif choice == '2':
            scientific_calculator()
        elif choice == '3':
            memory_store()
        elif choice == '4':
            memory_recall()
        elif choice =='5':
            show_history()
        elif choice =='6':
            print ("existing the calculator.....")
            break
        else :
            print("invalid choice")


if __name__ == "__main__":
    main()
