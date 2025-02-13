# Tuples are lists that you can't change, that's why it's faster and they are immutable.
friends = ['John','Michael','Terry','Eric','Graham']
# use regulare paranthesis instead of square bracket makes tuples
friends_tuple = ('John','Michael','Terry','Eric','Graham')

print(friends)
print(friends_tuple)


print(friends[2])
print(friends_tuple[2])

print(friends[2:4])
print(friends_tuple[2:4])
# If you want to change it you will have to create a new tuple and save the old one into it.
# Iterations or searches are faster in tuples than regular lists.
# When you can use it? When you have a list and do not want to change during your program.