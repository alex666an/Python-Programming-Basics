city = input()
sales_volume = float(input())
comission = 0
if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        comission = 0.05
        print(f'{sales_volume * comission:.2f}')
    elif 500 < sales_volume <= 1000:
        comission = 0.07
        print(f'{sales_volume * comission:.2f}')
    elif 1000 < sales_volume <= 10000:
        comission = 0.08
        print(f'{sales_volume * comission:.2f}')
    elif sales_volume > 10000:
        comission = 0.12
        print(f'{sales_volume * comission:.2f}')
    else:
        print('error')

elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        comission = 0.045
        print(f'{sales_volume * comission:.2f}')
    elif 500 < sales_volume <= 1000:
        comission = 0.075
        print(f'{sales_volume * comission:.2f}')
    elif 1000 < sales_volume <= 10000:
        comission = 0.1
        print(f'{sales_volume * comission:.2f}')
    elif sales_volume > 10000:
        comission = 0.13
        print(f'{sales_volume * comission:.2f}')
    else:
        print('error')

elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        comission = 0.055
        print(f'{sales_volume * comission:.2f}')
    elif 500 < sales_volume <= 1000:
        comission = 0.08
        print(f'{sales_volume * comission:.2f}')
    elif 1000 < sales_volume <= 10000:
        comission = 0.12
        print(f'{sales_volume * comission:.2f}')
    elif sales_volume > 10000:
        comission = 0.145
        print(f'{sales_volume * comission:.2f}')
    else:
        print('error')
else:
    print('error')






