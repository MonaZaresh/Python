# Loops are codes that run again and again, until some condition tells it to stop.
# below we have a pattern.
print("1.*Loops are great*")
print("2.**Loops are great**")
print("3.***Loops are great***")
print("4.****Loops are great****")
print("5.*****Loops are great*****")

# syntax of while loop
# while condition:
#     code
#     iterator or counter that you are going to increase or decrease oe whatever the case might be
# every time you wanna use a loop, you wanna ask yourself three questions
# we call them the three loop questions.

# Three Loop Questions:
#1. What do I want to repeat?
#  -> here: the message
#2. What do I want to change each time?
#  -> here: the stars 
#3. How long should we repeat?
#  -> here: 5 times

i=0
while i < 5:
    # i=i+1
    i+=1
    print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)
