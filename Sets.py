#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
# Curly bracket
# Sets are unordered-removes any duplicated that are inside it
# only one of each thing can exist in a set 
# Sets are a lot faster at finding members 
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends)
print(friends_tuple)
print(friends_set)


my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
# Items that are in both 
print(friends_set.intersection(my_friends_set))
# Items that are not in both
print(friends_set.difference(my_friends_set))
# a set with all the names in both of with no duplicates
print(friends_set.union(my_friends_set))



#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()