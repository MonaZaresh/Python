my_file = open(r"E:\UKSample\Fibonatchi\src\Python\LaernPython\greeting.txt",'r') #w, a
print(my_file.read())     # read all file
print(my_file.read(10))   # specify how many characters want read - ten first character
print(my_file.readline()) # read line by line

# read and structure the whole thing and break it up line by line
# there are two different ways:
line_by_line = my_file.readlines()
line_by_line1 = my_file.read().splitlines()
print('readlines: ',line_by_line)
print('splitlines: ',line_by_line1)
# when we open files, we always close the file 
# good rule to do this is to always write below command right after open the file 
# and put all the stuff you want to do in between(open&close)
my_file.close()


# there is another way for it:
# there is no need to close file explicity - it has implicity itself:
with open(r"E:\UKSample\Fibonatchi\src\Python\LaernPython\friends.csv",'r') as f: # f means file, csv is a comma separate file
    print(f.read()) # print as a long string
    friends = f.read().splitlines() # separat line by line
    print(friends) # print as a list
    for friend in friends:
        friend = friend.split(',') # separate by comma
        name = friend[0] # first item in each line
        year = int(friend[1].strip()) # second item which is integer and we should remove additional space
        print(f'In 2030 {name} will be {2030 -year} years old')


# we can use a loop and iterate through the lines of the file and print it out:
with open(r"E:\UKSample\Fibonatchi\src\Python\LaernPython\movies.txt",'r') as f:
    #for line in f: #not in scrimba
    for line in f.readlines(): #Scrimba workaround
        print(line)