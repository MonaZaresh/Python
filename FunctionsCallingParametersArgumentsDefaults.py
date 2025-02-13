# we use function to make it easier to reuse later
# def means define
# def greeting(name,age):
def greeting(name,age="28"): # set default value for age
    print("Hello " + name + ", you are " + age + "!")
    print(f"Hello {name}, you are {age}!")
    
name = input("Enter your name: ")    
greeting(name,"32")
greeting("Judith") # if we don't get the age it reads default value.


######## complete with String conversion ############

def greeting(name,age=28):
    print("Hello " + name + ", you are " + str(age) + "!")
    print(f"Hello {name}, you are {age}!")

name = input("Enter your name: ")    
greeting(name,32)
greeting("Judith")