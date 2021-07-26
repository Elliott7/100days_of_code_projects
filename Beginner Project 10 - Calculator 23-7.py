"""
Project Number Ten - Calculator
A functioning calculator. Prompts user for numerical input, asks what operation they would like to complete, returns
the result
"""

logo = """
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


def get_user_input(re_use=None):
    """
    Prompts the user for their input and returns both values, along with the operator that they would like to use

    """
    while True:
        if re_use is None:
            pass
        else:
            num1 = re_use
            break
        try:
            num1 = float(input("What's the first number?\n"))
            break
        except ValueError:
            print("Please enter a valid number")

    while True:
        operation = input("What operation would you like to do? \n+\n-\n*\n/\n")
        if operation == '+' or operation == '-' or operation == '*' or operation == '/':
            break
        else:
            print('Please enter a valid operator')
            continue

    while True:
        try:
            num2 = float(input("What's the second number?\n"))
            break
        except ValueError:
            print("Please enter a valid number")

    # This option works, however a function is included below that does not use eval()
    # eval_route = str(num1) + operation + str(num2)
    # print(eval(eval_route))
    return num1, operation, num2


def calculate(number1, operation, number2):
    """
    Computes the calculation and returns the result
    """
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        try:
            return number1 / number2
        except ZeroDivisionError:
            print("Cannot divide a number by 0")
    else:
        return "Error with operator"


def run_again(previous_answer):
    """
    Asks the user whether they would like to make another calculation using the previous result
    """
    while True:
        go_again = input(f"Type 'y' to continue with calculating with {previous_answer}, or type"
                     f" 'n' to start a new calculation\n")
        if go_again == 'y':
            return previous_answer
        elif go_again == 'n':
            return None
        else:
            print("Please enter either 'y' or 'n")


def main():
    while True:
        n1, op, n2 = get_user_input()
        result = calculate(n1, op, n2)
        print(f"The answer is: {result}")
        if run_again(result) is None:
            continue
        while True:
            n1, op, n2 = get_user_input(result)
            result = calculate(n1, op, n2)
            print(f"The answer is:{result}")
            if run_again(result) is None:
                break


if __name__ == "__main__":
    main()
