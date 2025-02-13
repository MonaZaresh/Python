#Python 101: String Exercise 1
#1. From the string "Welcom to Python 101: Strings", extract text and create/print a new string that says 
# * "1 Welcom Ring To Tyler"
# * Every first letter in a word should be capitalized(title format)

# 2. Print the same string backwards...
# Hint: Google is your friend

msg='welcome to Python 101: Strings'
  
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())
# string backwards
print(msg1[::-1].title())