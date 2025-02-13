# Dictionaries store name value pairs or key value pairs.
# that is square bracket : []
# that is curly bracket {}
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
print(movie)
print(movie['title'])
print(movie['budget']) # ask about something does not exist : we get an error!
# to prevent getting error we can use get method
print(movie.get('budget')) # we get back None.
# None is an empty object 
# Even we can set a default value, with get function:
print(movie.get('budget','not found'))


# We can update a dictionary with square bracket notation we can specify what value I want to update

movie['title'] = 'The Holy Grail'
print(movie.get('title'))
# or even add something new to the dictionary:
movie['budget'] = 250000
print(movie.get('budget')) # new entry


# we can update the whole dictionary:
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})


# we can delete entries from the dictionary:
del movie['year']
print(movie)

# a more often used and more useful way to remove values while at the same time 
# using the value in my code is to use pop command(we used for lists as well):
year = movie.pop('year')
print(movie)
print(year)


# How many entries there are - we can ask for length(same as in the lists):
print(len(movie))


# dictionary keys
print(movie.keys())

# dictionary values
print(movie.values())

# the result is a tuple
print(movie.items())

# you can loop through all the items in a dictionary:
for key in movie:
    print(key)

for key, value in movie.items():
    print(key, value)