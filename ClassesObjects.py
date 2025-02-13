print("Classes & Objects")
# A class is a custom made dattype that allows you to do that.
# Classes are representation of the abstract concept of something like a blueprint.
# class has a variable which is called attribute, functions inside a class is method.

#Classes are blueprints
#Objects are the actual things you built
#variables => attributes
#functions => methods
#class should be CamelCase - every new word starts with a capital letter.

# in the class when I create new object, that is the self.
class Movie:
    # self is a key word, refers to the object that I'm creating.
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)
        
film_1 = Movie("Life of Brian",1979,8.1,True)
film_2 = Movie("The Holy Grail",1975,8.2,True)

#print(film_1.title, film_1.imdb_score)
film_2.nice_print() # the argument is implicit in this call
# this is equivalent of this line:
Movie.nice_print(film_2)


# or even do this the following like a database!
films = [film_1,film_2]
print(films[1].title,films[0].title)
films[0].nice_print()