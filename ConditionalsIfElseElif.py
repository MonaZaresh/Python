# with If statement, our programe can make decisions.
# It can run different code depending on different circumastances

print("Conditionals: IF statements")

# if I can't hold my breath anymore = True
# then stop holding breath and come up

is_raining = True
print("Good Morning!")
if is_raining: 
    print("Bring umbrella!")



    is_raining = False
print("Good Morning!")
if is_raining: 
    print("Bring umbrella!")
else:
    print("Umbrella optional!")


# introduce OR statement
is_raining = True
is_cold = True # / False
print("Good Morning!")
if is_raining or is_cold: 
    print("Bring umbrella or jacket or both!")
else:
    print("Umbrella optional!")


is_raining = False
is_cold = False
print("Good Morning!")
if is_raining or is_cold: 
    print("Bring umbrella or jacket or both!")
else:
    print("Umbrella optional!")



# And operator
is_raining = False # / True
is_cold = False
print("Good Morning!")
if is_raining and is_cold: # it has to be both are true!
    print("Bring umbrella or jacket or both!") # true and true
else:
    print("Umbrella optional!")



is_raining = True
is_cold = True
print("Good Morning!")
if is_raining and is_cold: 
    print("Bring umbrella and jacket!")
else:
    print("Umbrella optional!")


# another logical operator >> NOT
is_raining = True
is_cold = True # False
print("Good Morning!")
if is_raining and is_cold: 
    print("Bring umbrella and jacket!")
elif is_raining and not(is_cold):
    print("Bring umbrella!")
elif not(is_raining) and is_cold:
    print("Bring jacket!")
else:
    print("Umbrella optional!")


    is_raining = False
is_cold = False
print("Good Morning!")
if is_raining and is_cold: 
    print("Bring umbrella and jacket!")
elif is_raining and not(is_cold):
    print("Bring umbrella!")
elif not(is_raining) and is_cold:
    print("Bring jacket!")
else:
    print("Shirt is fine!")



amount = 10
if amount <= 50:
    print("Purchase approved")
else:
    print("Please enter your PIN")