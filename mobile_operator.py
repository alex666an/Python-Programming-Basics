fee = 0
mobile_internet_price = 0
contract_length = input()
contract_type = input()
mobile_internet = input()
payment_days = int(input())
if contract_length == 'one':
    if contract_type == 'Small':
        fee = 9.98
    elif contract_type == 'Middle':
        fee = 18.99
    elif contract_type == 'Large':
        fee = 25.98
    elif contract_type == 'ExtraLarge':
        fee = 35.99
elif contract_length == 'two':
    if contract_type == 'Small':
        fee = 8.58
    elif contract_type == 'Middle':
        fee = 17.09
    elif contract_type == 'Large':
        fee = 23.59
    elif contract_type == 'ExtraLarge':
        fee = 31.79
if mobile_internet == 'yes':
    if fee <= 10:
        mobile_internet_price = 5.5
    elif fee <= 30:
        mobile_internet_price = 4.35
    elif fee > 30:
        mobile_internet_price = 3.85
total = fee + mobile_internet_price
if contract_length == 'two':
    total *= 0.9625
total_payment = total * payment_days
print(f'{total_payment:.2f} lv.')
