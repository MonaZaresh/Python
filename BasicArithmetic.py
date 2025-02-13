# https://www.pythoncheatsheet.org/cheatsheet/basics

print("Basic Arithmetic") # Math operators
a=6
b=2
# From highest to lowest precedence
print('Exponent : ', a ** b)
print('Modulus : ', a % b)
print('Division (floor) : ', a // b)
print('Division (float) : ', a / b)
print('Multiplication : ', a * b)
print('Subtraction : ', a - b)
print('Addition : ', a + b)

#Augmented Assignment Operators
# Operator	Equivalent
# var += 1	var = var + 1
# var -= 1	var = var - 1
# var *= 1	var = var * 1
# var /= 1	var = var / 1
# var //= 1	var = var // 1
# var %= 1	var = var % 1
# var **= 1	var = var ** 1

greeting = 'Hello'
greeting += ' world!'
print(greeting)
# 'Hello world!'

my_list = ['item']
my_list *= 3
my_list
# ['item', 'item', 'item']