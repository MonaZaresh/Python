# You sell lemonade over two weeks, the lists show number of lemonades sold per week
# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# Profit for each lemonde sold is 1.5$
# Add another day to week 2 list by capturing a number as input
# Combine the two lists into the list called 'sales'
# Calculate/ print how much you have earned on
# . Best day
# . Worst day
# . Separately and in total
#Hint: 3 prints in total

# Mona Solution
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

num1=input('insert day for week 2: ')
sales_w2.append(int(num1))
print(sales_w2)

sales.extend(sales_w1)
sales.extend(sales_w2)
print(sales)


best_w1=max(sales_w1) * 1.5
best_w2=max(sales_w2) * 1.5

worst_w1=min(sales_w1) * 1.5
worst_w2=min(sales_w2) * 1.5
salesweeks_total = f"""On best day in week one I have earned {best_w1} and on worst day I\'ve earned {worst_w1}
while, for week 2 they are respectively {best_w2} and {worst_w2}"""
print(salesweeks_total)
total_earn= f'Totally I\'ve earned {max(sales) * 1.5} as a Best day. But, I\'ve just eraned {min(sales) * 1.5} as a Worst day.'
print(total_earn)



# Toturial Solution
# new_day = input('Enter #of lemonades for new day: ')
# sales_w2.append(int(new_day))
# sales.extend(sales_w1)
# sales.extend(sales_w2)
# sales = sales_w1 + sales_w2
# sales.sort()
# worst_day_prof = sales[0] * 1.5
# best_day_prof = sales[-1] * 1.5
# #sales.sort()
# # worst_day_prof = min(sales) * 1.5
# # best_day_prof = max(sales) * 1.5
# print(f'Worst day profit:$ {worst_day_prof}')
# print(f'Best day profit:$ {best_day_prof}')
# print(f'Combined profit:$ {worst_day_prof + best_day_prof}')