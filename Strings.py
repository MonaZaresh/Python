
msg='welcome to Python 101: Strings'
#msg='welcome to it\'s Python 101: Strings'
print(msg)
print(msg+msg)
print(msg*2)
print(msg,msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(len(msg))
print(msg.count('python'))#case insensitive >> Python - o
#slicing - is getting parts of a string
# square brackets
print(msg[0])   # 5 > m
print(msg[-1])  # the last character #-3
print(msg[2:])  # colon will tell the Python to grab everything after the number 2 string
print(msg[2:7]) # 7 not inclusive - it takes up to that, but it does not actually takes the seventh one.
print(msg[:7])