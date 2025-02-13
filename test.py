# val = 'mona'
# print(val[::-1])

# for digit in range(1,-1,-1):
#     print(digit)

for digit in range(1,0,-1):
    for dig2 in range(1,-1,-1):
        for dig3 in range(1,-1,-1):
            # palindrome = digit*100000 + dig2*10000 + dig3*1000 + digit*100 + dig2*10 + dig3
            palindrome2 = digit*100000 + dig2*10000 + dig3*1000 + dig3*100 + dig2*10 + digit
            print(palindrome2)