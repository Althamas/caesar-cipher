from replit import clear
print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
)
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculation():
    num1 = float(input("Enter your first number: "))
    for s in operations:
        print(s)
    cont = True
    while cont:
        op = input("Pick an operation: ")
        num2 = float(input("Enter your next number: "))
        ope = operations[op]
        answer = ope(num1,num2)
        print(f"{num1} {op} {num2} = {answer}")
        if input(f"Type 'y' to continue with {answer} or 'n' to begin new calculation: ") == 'y':
            num1 = answer
        else:
            cont = False
            print("Thank You")
            clear()
            calculation()

calculation()