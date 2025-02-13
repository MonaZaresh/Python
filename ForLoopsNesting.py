# In while loop you know the number of iterations a for loop will perform beforehand 
# which isn't always the case with a  while loop 
# Most of the time for loops are used for looping through all the letters, all the objects, members or 
# whatever in a string list or something else 
# I'm not sure how many I need to do so 
# I'd better stop or continue after each one loop can be linked a bit to a while loop 

#fek konam, yani baraye while ma nemidonim cheqadr bayad tekrar konim vali baraye for az qabl midonim!!!

# For syntax:
# letter is variable
# for letter in 'Norwegian blue':
#     print(letter)
for furgle in 'Norwegian blue':
    print(furgle)

print("For Loop done!")

for furgle in range(8): # numbers from 0 up to 8,  not including 8!
    print(furgle)

for furgle in range(2,8):
    print(furgle)

# you can also use step:
for furgle in range(1,15,3): # strat from one, run to 15, do in steps of three
    print(furgle)

# you can do this in a list
for name in ['John','Terry','Eric','Michael','George']:
    print(name)

# we can move these names to a variable 
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    print(friend)

# we can also specify the number by finding it out by using the length of the list
friends = ['John','Terry','Eric','Michael','George']
for index in range(len(friends)):
   print(friends[index])

# break and continue statement
# break statement takes you out of a loop 
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '!')
        break
    print(friend)

# continue statement allows you to continue when something happens inside your loop.
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '!')
        continue
    print(friend)

# nested loop (a loop inside another loop)
friends = ['John','Terry','Eric']
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)