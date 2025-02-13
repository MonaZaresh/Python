
# optimize/shorten the code in the function
# try to reduce the number of conditionals 

def num_days(month):

    if month == 'jan':
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    elif month == 'mar':
        print('number of days in',month,'is',31)
    elif month == 'apr':
        print('number of days in',month,'is',30)
    elif month == 'may':
        print('number of days in',month,'is',31)
    elif month == 'jun':
        print('number of days in',month,'is',30)
    elif month == 'jul':
        print('number of days in',month,'is',31)
    elif month == 'aug':
        print('number of days in',month,'is',31)
    elif month == 'sep':
        print('number of days in',month,'is',30)
    elif month == 'oct':
        print('number of days in',month,'is',31)
    elif month == 'nov':
        print('number of days in',month,'is',30)
    elif month == 'dec':
        print('number of days in',month,'is',31)

num_days('oct')

# Solution
def num_days(month):

    # if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
    #     print('number of days in',month,'is',31)
    # elif month == 'feb':
    #     print('number of days in',month,'is',28)
    # # First :
    # # elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
    # #     print('number of days in',month,'is',30)
    # # Second:
    # else:
    #     print('number of days in',month,'is',30)

    # Third :
    # days = 31
    # if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
    #     days = 30
    # elif month == 'feb':
    #     days = 28
    # print('number of days in',month,'is',days)
    
    # Forth :
    days = 31
    # a list
    # if month in ['apr','jun','sep','nov']:
    # or a tuple which is slightly faster
    # if month in ('apr','jun','sep','nov'):
    # Also a set which is a lot faster and is optimized for membership checking:
    if month in {'apr','jun','sep','nov'}:
    #if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in',month,'is',days)


num_days('jul')

