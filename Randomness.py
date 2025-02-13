import random
# this module generate random number between 0 and 1
print(random.random())

#generate five random numbers:
for i in range(5):
    print(random.random())

# if I want to generate numbers between 1 to 6:
for i in range(5):
    print(random.random()*6)

# if I want to specify function for myself, I can use 
# uniiform function which takes two arguments: 
# the first one is the fisrt number it should start at
# generate a number between 1 to 6 :
for i in range(5):
    print(random.uniform(1,6))

# these numbers were float
# we can use another function to generate integer numbers which is similar to uniform function:
for i in range(5):
    print(random.randint(1,6))

# I can change it to be a range, third argument is the step
for i in range(5):
    print(random.randrange(1,100,2)) # odd numbers
    # print(random.randrange(1,100,2)) # even numbers 

# I can even choose random item from a list
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.choice(friends_list))

# for draw multiple names, use different function called: sample
# and define how many samples I want
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.sample(friends_list,3)) # it does not generate duplicate sample
# print(random.sample(friends_list,6)) # it'll raise error because it is bigger than the list
# print(random.sample(friends_list,5)) # I can only draw the whole list

random.shuffle(friends_list) # it can work with numbers and lists 
print(friends_list)







# I need another module called: string
import string
smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
# holding ascii constant
letters_numbers = string.ascii_letters + string.digits # contains both lowercase and uppercase
# letters_numbers = string.ascii_lowercase + string.digits
# letters_numbers = string.ascii_uppercase + string.digits
word = ''
for i in range(7):
    word = word + random.choice(letters_numbers)
    # word += random.choice(letters_numbers) # different notation to make a bit shorter
print(word)

# or instead of using for loop:
word1 = ''.join(random.sample(letters_numbers,7))    
print(word1)
    
# or even use this one instead of using join:
word = random.choices(letters_numbers, k=7)  # it can generate duplicate random!!