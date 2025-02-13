#list can contain a mix of variable types, string, boolean, float,..
friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
friends.sort() # sort ascending
print(friends)
friends.sort(reverse=True) #capital T is important, because it indicating a true statement for the Boolean
print(friends)#Sort in descenting order
# Reverse 
# reverse the string (not a reverse sorting descending)
# it just reverse the order of the original string.
friends.reverse()
print(friends)


cars.sort()
print(cars)
# these functions works on friends list as well!!
print(min(cars))
print(max(cars))
print(sum(cars))

friends.append('TerryG') # add an extra feiend at the end of the list 
# or insert at a certain point:
friends.insert(1,'TerryG')
friends[2]='TerryG' # it removed the last item and replace with the new one - not appended the list or added
friends.extend(cars)
print(friends)
# remove - we have to specify which one we want to remove
friends.remove('Terry')
print(friends)
# we can use pop function instead of remove
# by this function we pop it into memory so that you can use it in 
# grab the last or remove the last name in the array
friends.pop()
print(friends)
# you can specify what you want to pop
friends.pop(2)
friends.pop(-1)

# empty or clear the list
friends.clear()
print(friends)

# if you want remove it completely
del friends
print(friends) # we get an error

del friends[2] # we remove index 2

# copy list
# first way
new_friends = friends[:]
print(friends)
print(new_friends)

#second way
new_friends = friends.copy()

# third way
new_friends = list(friends)