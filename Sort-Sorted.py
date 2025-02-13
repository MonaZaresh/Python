# print('sort() and sorted()')
# print('Immutability and return values')

# Sort method doesn't actually return anything : 
#             it just does the work of sorting - So it goes in and sorts the list.
#             doesn't return a new list 
# Function sorted actually returns a new object that has been sorted.


my_list = [1,5,3,7,2] # Lists are mutable, we can change them, that's why they have a sorting method.
my_dict = {'car':4,'dog':2,'add':3,'bee':1} # Dictionaries - they are special and they are also mutable.
# Tuple and string do not have sort function as they are immutable
# If I want to change them I turn them into something new.
my_tuple = ('d','c','e','a','b') # immutable
my_string = 'python'  # immutable


# Sort method
print(my_list,'original')
print(my_list.sort())
print(my_list,'new')

# The same will happen with reverse:
print(my_list,'original')
print(my_list.reverse())
print(my_list,'new')


# Sorted function:
print(my_list,'original')
print(sorted(my_list))
# in realality something happens like this (creating new object):
# my_list1 =sorted(my_list)
# print(my_list1)
print(my_list,'new')


# when we sort a tuple we don't get actually a tuple, it is a list.
# my tuple is still the same that it was before.
print(my_tuple,'original')
print(sorted(my_tuple))
print(my_tuple,'new')

# again it is a list with individual letters sorted in order(ascending order)
print(my_string,'original')
print(sorted(my_string))
print(my_string,'new')


# sorted version in the middle (sorted key value - the first element- in an ascending order)
print(my_dict,'original')
print(sorted(my_dict))
#print(sorted(my_dict.items()))
#print(sorted(my_dict.values()))
#print(sorted(my_dict.values(), reverse=True))
print(my_dict,'new')


print(my_list,'original')
print(reversed(my_list))
#print(list(reversed(my_list)))
print(my_list,'new')

print(my_list,'original')
print(my_list[::-1])




# abs means absolute function
my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_list))
# sorted in the order of numbers regardless of whether it's a positive or negative number.
print(sorted(my_list, key = abs))

print(sorted(my_llist)) # it will sort with the first element.
# We have two types of functions, built-in or define our own function using a lambda
# lambda functions are throwaway functions that you can write on one line.

# item in the list that we are trying to sort - 
#                   item[] which is the list inside the list(which index in the list)
#                   we want to sort on the second element we can put 1 for second index
# print(sorted(my_llist, key = lambda item :item[1])) 
