# Party invitation
# You're having a party and want to invite your friends.
# you want the print out invitations for each friend using for loops
# the names are in two lists, 'names' and 'names1'
# you also need to add two extra names to the list using an 'input' box. when you run the code
# print out on invitation to each friend per line
# names should be properly capitalized 
# Example of printout
# John Cleese! You are invited to the party on Saturday.
# Eric Idle! You are invited to the party on Saturday.
# Hint: You may need two (for) loops to solve this exercise



#Mona Solution
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
invited_person = input('Invite one of you friends, write their name here: ')
names.append(invited_person)
invited_person1 = input('Invite another one, write their name here: ')
names1.append(invited_person1)

for person in names:
    print(f'{person.title() }! You are invited to the party on Saturday.')
for buddy in names1:
    print(f'{buddy.title() }! You are invited to the party on Saturday.')


# Course SOlution
msg = 'You are invited to the party on saturday.'
names.extend(names1)
#names = names + names1
#names += names1
for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    msg1 = f'{name.title()}! {msg}'
    #msg1 = name.title() + '! ' + msg
    print(msg1)