# print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

# Mona Solution
# num1=input('Enter #1 digit: ')
# num2=input('Enter #2 digit: ')
# operator=input('Choose the operator: +,-,*,/:')
# if(operator == '+'):
#     print(f'The result of addition is : {round(float(num1)+float(num2),2)}')
# elif(operator == '-'):
#     print(f'The result of addition is : {round(float(num1)-float(num2),2)}')
# elif(operator =='*'):
#     print(f'The result of addition is : {round(float(num1)*float(num2),28)}')
# elif(operator == '/'):
#     print(f'The result of addition is : {round(float(num1)/float(num2),2)}')

# difference between if and elif
# if we run ifs each one of the ifs will get checked
# while if we use elifs, it will only check until 
# it finds something that is correct and it stops and exits the conditionals.

# Course Solution
mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!')