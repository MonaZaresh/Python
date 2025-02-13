# print('Comparisons')
a = 7
b = 3
print(a == b) # we are asking if a is equal to b
print(a != b) # for checking to not equal 
print(a > b) # greater than
print(a < b) # less than
print(a <= b) # less than or equal
print(a >= b) # greater than or equal
print('o' in 'John') # it is in 
print('o' not in 'John') # it is not in (not found)
# checks if two values are identical

a = [3,7,42]
b = a
# they occupying the same memory space in the computer
print(a == b)
print(a is b) # are they identical, are they the same thing?
print(id(a), id(b)) 


# below they have a same value but not the same in memory
a = [3,7,42]
b = [3,7,42]
print(id(a), id(b)) 



a=7
b=3
print('a == b is', a == b)
print('a != b is', a != b)
print('a > b is', a > b)
print('a < b is', a < b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)
print('o in John is ','o' in 'John') #membership
print('o in John is ','o' not in 'John') #non membership
print('John is John ','John' is 'John') #identity
print('John is not John is ','John' is not 'John') # negative identity



print(int(True))  # 1
print(int(False)) # 0
# empty objects or zeros evaluate to false and everything else seems to evaluate to true
print(bool('Parent')) # True
print(bool('')) # white space evalutes to False
print(bool(42)) # True
print(bool(1))  # True
print(bool(0))  # False
print(bool([1,2])) # True
print(bool([]))    # empty liste evaluate to False
                   # Boolean values can actually be converted to one and zero
print(42 +True)    # 4number 42 plus true, we get 43
print(42 + False)  # we get 42, it adds zero 