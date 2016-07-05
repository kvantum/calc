operators = ['+', '-', '*', '/']
def input_numbers():
    """
    Reads numbers and operator from the console. Converts numbers to float.
    :return: list with 3 elements: two numbers and operator
    """
    print('------ This is the simple calculator -----------')
    while True:
        try:
            num1 = float(input('Enter the first number:'))
            break
        except:
            print('Try again. Enter a number, please.')

    while True:
        try:
            num2 = float(input('Enter the second number:'))
            break
        except:
            print('Try again. Enter a number, please.')

    operator = raw_input('Choose the operation (+, -, *, /):')
    inp_data = [num1, num2, operator] #list with entered data
    return inp_data


def calculate(numb):
    """
    Calculates the result of the operation.
    :param numb: a list with 3 elements: two numbers and operator
    :return: result of the operation
    """
    oper = numb[2]
    result = {'+': numb[0] + numb[1],
              '-': numb[0] - numb[1],
              '*': numb[0] * numb[1],
              '/': numb[0] / numb[1]
              }
    print('Result of the operation:')
    res = str(numb[0]) + ' ' + oper + ' ' + str(numb[1]) + ' = ' \
          + str(result[oper])
    print(res)
    return result[oper]

inp_data = input_numbers()

# Check if the correct operation entered.
while True:
    if inp_data[2] == '/' and inp_data[1] == 0:
        print('Division by zero. Try again.')
        print('')
        input_numbers()
    elif inp_data[2] not in operators:
        print('Hey, You can use only these operations: +, -, *, /')
        inp_data[2] = raw_input('Choose the operation (+, -, *, /):')
    else:
        break

calculate(inp_data)
