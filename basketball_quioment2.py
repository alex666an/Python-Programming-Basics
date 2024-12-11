annual_fee = int(input())
sneakers = annual_fee * 0.6
equipment = sneakers * 0.8
ball = equipment / 4
accessories = ball / 5
print(f'{sneakers + equipment + ball + accessories + annual_fee:.2f}')
