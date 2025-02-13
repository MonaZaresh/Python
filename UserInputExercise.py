# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

#My try
# name=input('Give me your first name: ')
# num1=input('insert the distance in KM: ')
# km_to_mile= float(num1)/1.609
# print('Hello '+ name.capitalize() + ', the ' + num1 + ' is equal ' + str(km_to_mile))

name = input('Enter your name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609
print(f'Hi {name.title()}! {distance_km}km is equivalent to {distance_mi} miles.')
print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')
