# allows me to write single line function definitions that 
# might just use once and throw away or use multiple time
print(' Lambda Functions')
def square(x):
    return x*x
print(square(3))

# syntax:
# name = lambda parameter(s): expression 
# lambda is a keyword, then specify the paramater I want to use, then actual expression
square1 = lambda x: x*x # return value is implicit in a lambda function always 
# lambda always returns a value while a function don't have to return a value
print(square1(3))


double_mult = lambda x,y: 2*x*y
print(double_mult(2,3))


# let's try a different scenario
# name strip out any spaces or trailing spaces, also titleize it
def name_and_alias(name,alias):
    return name.strip().title() + ':' + alias.strip().title()

print(name_and_alias(' john  ClEEse  ','HECKLER'))

# now let's try by lambda:
name_and_alias1 = lambda name,alias:name.strip().title() + ':' + alias.strip().title()

print(name_and_alias(' john  ClEEse  ','HECKLER'))
print(name_and_alias1(' john  ClEEse  ','HECKLER'))

#define method/function in one line:
def name_and_alias2(name,alias):return name.strip().title() + ':' + alias.strip().title()
print(name_and_alias2(' john  ClEEse  ','HECKLER'))




monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
monty_python.sort(key = lambda name:name.split(' '))     # order by the first name
monty_python.sort(key = lambda name:name.split(' ')[-1]) # order by last name
print(monty_python)

# I can do the same thing by define a function:
def sort_names(name):
    return name.split(' ')
monty_python.sort(key = lambda name:name.split(' ')[-1]) # sort by last name
print(monty_python)
monty_python.sort(key= sort_names) # sort by first name
print(monty_python)
