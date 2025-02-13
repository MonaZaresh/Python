friends = ['John','Michael','Terry','Eric','Graham'] # we can use index 
print(friends)
print(friends[1],friends[4])
print(friends[-1])
print(friends[2:4]) # not printing the actual number four, just like strings!
print(friends[:4]) # if we don't have a first number, it will assume that we mean from the start of the string
print(friends[:]) # we get the whole list
print(len(friends))
print(friends.index('Eric'))
print(friends.count('Eric'))# we count the number of occurrences of Eric
