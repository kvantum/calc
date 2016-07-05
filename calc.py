operators = ['+', '-', '*', '/']
def input_numbers():
    global num1, num2, operator, result
    num1 = float(input('Enter the first number:'))
    num2 = float(input('Enter the second number:'))
    
    operator = raw_input('Choose the operation (+, -, *, /):')


def calculate(number1, number2):
    global result
    result = {'+': number1 + number2,
              '-': number1 - number2,
              '*': number1 * number2,
              '/': number1 / number2
              }
    print(str(number1) + ' ' + operator + ' ' + str(number2) + ' = ' + str(result[operator]))
    return result

input_numbers()
while True:
    if operator == '/' and num2 == 0:
        print('Division by zero. Try again.')
        print('')
        input_numbers()
    elif operator not in operators:
        print('Hey, You can use only these operators: +, -, *, /')
        operator = raw_input('Choose the operation (+, -, *, /):')
    else:
        break
calculate(num1, num2)
