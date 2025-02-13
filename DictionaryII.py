python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}


# like sets, dictionaries are not ordered and 
# can't contain duplicate values at least at the keys but in the values they can contain duplicate values



#membership test
print('arthur' in holy_grail) # it is case sensitive: Arthur - arthur

if 'Arthur' not in python: # if 'Arthur' in python:   nothing happen here!
    print('He\'s not here!')

# concatenating or putting several dictionries together:


# First way/method is update:
# if we have two dictionary, the regular update works fine. 
# even there is no need to create a new one, I can use the existing dictionary.
people = {} # empty dictionay
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(people)



# method 2 comprehension
# if I want to do for more than two dictionary 
people1 = {}
for groups in (python,holy_grail,life_of_brian) : people1.update(groups)
print(people1)



#method 3 unpacking 3.5 later
# if I want to do for more than two dictionary 
people2 = {}
people2 = {**python,**holy_grail,**life_of_brian}
print(people2)

# dictionaries are inherently not sorted or ordered
print(sorted(people)) # it returns just keys 
# for all items, we need this command:
print(sorted(people.items()))


# sum over a dictionary:
print('The sum of the ages: ', sum(people.values())) # if the value be a string it makes crash and error!
