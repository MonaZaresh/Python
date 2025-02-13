msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(list(msg)) # Split one by one character
print(msg.split()) # Separated by white spaces- it does not care multiple spaces or white spaces involved
print(msg.split(' ')) # On what type of character it should split-it shows empty strings
print(msg.split(' '), type(msg.split(' ')))
print(msg.split(','), type(msg.split(' ')))
print(csv.split(',')) # comma separator into a list

#join that into a string- it looks like a list but it's actually string
print(str(friends_list))

print('-'.join(friends_list))
print('-'.join(friends_list + friends_list))
print(''.join(friends_list))

print(''.join(msg.split()))
print(msg.replace(' ', ''))