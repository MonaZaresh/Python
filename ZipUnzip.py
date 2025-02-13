# I can combine different iterables which are strings, tuples, lists, things I can iterate through
# combine three below lists with zip command in different ways:
nums = [1,2,3,4] 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']

# combo = zip(nums,letters) # it returns zip object, I cannot see what is inside it.
combo = list(zip(nums,letters)) # list of tuples, they are matched by index number (zip does it)
# if there are two iterables of the same length it's going to match them
print(combo) 



#even by changing it to the string it will work
nums = '1234' 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']
combo = dict(zip(nums,letters))
print(combo)





# I can also add even more of these iterables
nums = '1234' 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']
combo = list(zip(nums,letters,names))
print(combo)


# unzipped - unpacking
num,let,nam =zip(*combo) # assign the result of this unzip into three different variables
# asterisk *
print(num,let,nam)







#special case with dictionaries
keys = 'this parrot is deceased'
values = 'denna papegojan är avliden' #Swedish
# it is not easy to iterate over since they have the space inside them and 
# it's not obvious where they're actually separated, split them into a list:
keys = keys.split()
values = values.split()
print(keys,values)
# below: dictionary comprehension = similar to list comprehension
en_sv_dict = dict(zip(keys,values))
print(en_sv_dict)
# different way:
new_dict = {key:value for key,value in zip(keys,values)}
print(new_dict)
# separate from each other:
en,sv = list(en_sv_dict.keys()),list(en_sv_dict.values())
print(en,sv)
# another way:
en1,sv1 = zip(*en_sv_dict.items()) # item contains all the items
print(en1,sv1)