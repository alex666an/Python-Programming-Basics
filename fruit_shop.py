fruit = input()
day_of_week = input()
quantity = float(input())
price= 0
if day_of_week == 'Monday' or day_of_week == 'Tuesday' \
        or day_of_week == 'Wednesday' or day_of_week == 'Thursday' \
        or day_of_week == 'Friday':
    if fruit == 'banana':
        price = 2.5
        print(f'{quantity * price:.2f}')
    elif fruit == 'apple':
        price = 1.2
        print(f'{quantity * price:.2f}')
    elif fruit == 'orange':
        price = 0.85
        print(f'{quantity * price:.2f}')
    elif fruit == 'grapefruit':
        price = 1.45
        print(f'{quantity * price:.2f}')
    elif fruit == 'kiwi':
        price = 2.7
        print(f'{quantity * price:.2f}')
    elif fruit == 'pineapple':
        price = 5.5
        print(f'{quantity * price:.2f}')
    elif fruit == 'grapes':
        price = 3.85
        print(f'{quantity * price:.2f}')
    else:
        print('error')
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        price = 2.7
        print(f'{quantity * price:.2f}')
    elif fruit == 'apple':
        price = 1.25
        print(f'{quantity * price:.2f}')
    elif fruit == 'orange':
        price = 0.90
        print(f'{quantity * price:.2f}')
    elif fruit == 'grapefruit':
        price = 1.60
        print(f'{quantity * price:.2f}')
    elif fruit == 'kiwi':
        price = 3
        print(f'{quantity * price:.2f}')
    elif fruit == 'pineapple':
        price = 5.6
        print(f'{quantity * price:.2f}')
    elif fruit == 'grapes':
        price = 4.2
        print(f'{quantity * price:.2f}')

    else:
        print('error')




