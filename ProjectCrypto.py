# print('Project -  Crypto')
# Steps:
def enigma_light():
    # 1-create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    # 2-autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    # now I have two lists : original list, the offset list
    # print(keys)
    # print(values)
# create two dictionaries - for encryption and decryption
# first solution:
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys)) 
# second solution: # OR create 1 and then flip (dictionary comprehension)
# by changing the dictionary so that the key becomes the value and the value becomes the key:
    # dict_e = dict(zip(keys,values))
    # dict_d = {value:key for key, value in dict_e.items()}
#user input 'the message' and mode - for encrypt and decrypt
    msg = input('Enter your secret message quietly: ').lower()
    mode = input('Crypto mode: encode (e) OR decode (d): ')
# run encode or decode
    if mode.lower() == 'e':
        # new_msg = [dict_e[letter] for letter in msg] # it reurnslist
        # change to plain text-convert list to string by join command:
        new_msg = ''.join([dict_e[letter] for letter in msg])
    elif mode == 'd':
        # new_msg = [dict_d[letter] for letter in msg]
        new_msg = ''.join([dict_d[letter] for letter in msg])

    
    return new_msg
# return result
# clean and beautify the code 
print(enigma_light())














# clean and beautify message:
def enigma_light():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys)) 
    msg = input('Enter your secret message quietly: ').lower()
    mode = input('Crypto mode: encode (e) OR decrypt as default: ')
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg])
    
    return new_msg.capitalize()

print(enigma_light())