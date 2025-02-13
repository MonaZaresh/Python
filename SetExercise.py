#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

#My Solution
print(friends.__contains__('Eric'))
print(friends.__contains__('John'))
# Course Solution
print('Eric' in friends and 'John' in friends)

# For union we can use | 
print(friends.union(my_friends))
print(friends | my_friends)

# For finding common items we can use & too.
print(friends.intersection(my_friends))
print(friends & my_friends)

# for finding something that just exist in first set we can use subtraction!!
print(friends.difference(my_friends))
print(friends - my_friends)

#Show only the names who only appear in one of the lists
# it shows all of the different items or members that exist in just one of the sets
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)

# My solution
print(set(cars))
# Course solution:
cars_no_dupl =set(cars)
#cars_no_dupl =list(set(cars)) # back into the list without duplicate items.
print(cars_no_dupl)