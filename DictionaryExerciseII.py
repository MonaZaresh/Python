freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}


#V1.2
cart = {}
for shop in (freelancers,antiques,pet_shop) :
    buy_item = input(f'Welcome to {shop["name"]}! what do you want to buy: {shop}').lower()
    if buy_item == 'exit':
        continue # leave the store and go o the next shop
    if buy_item not in shop: # test membership
        continue
        
    cart.update({buy_item:shop.pop(buy_item)})
    buy_items = ", ".join(list(cart.keys()))
print(f'You Purchased {buy_items}. Today it is all free. Have a nice day of mayhem!')




cart = {}
#create purse with 100Gp (gold pieces)
purse = 1000
for shop in (freelancers,antiques,pet_shop) :
    buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit store) what do you want to buy: {shop}').lower()
    #exit on exit typed or buying nonexistant item
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        continue
        
    cart.update({buy_item:shop.pop(buy_item)})
    buy_items = ", ".join(list(cart.keys()))
    #Calling sum twice is not optimal
# print(f'You Purchased {buy_items}. Your total is {sum(cart.values())} Gp. 
#       Your change is {purse - sum(cart.values())} Gp. Have a nice day of mayhem!')
#Solution
    total_sum = sum(cart.values())
print(f'You Purchased {buy_items}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')



# It is the same but has more information:
cart = {}
#create purse with 100Gp
purse = 1000
buy_items1 = ''
#loop through stores/dicts
for shop in (freelancers,antiques,pet_shop) :
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit store) what do you want to buy: {shop}').lower()
    #exit on exit typed or buying nonexistant item
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        continue
    #update string
    buy_items1 = buy_items1 + f'{buy_item}:{shop[buy_item]} Gp, '    
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
    buy_items = ", ".join(list(cart.keys()))
    total_sum = sum(cart.values())
print(f'You Purchased {buy_items}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
print(f'You Purchased {buy_items1}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')