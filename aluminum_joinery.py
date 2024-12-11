joinery_count = int(input())
joinery_size = input()
shipment_method = input()
price_for_one = 0
delivery_price = 0
discount = 0
total_price = 0
if joinery_size == '90X130':
    price_for_one = 110
    if 60 > joinery_count > 30:
        discount = 0.05
    elif joinery_count > 60:
        discount = 0.08

elif joinery_size == '100X150':
    price_for_one = 140
    if 80 > joinery_count > 40:
        discount = 0.06
    elif joinery_count > 80:
        discount = 0.1

elif joinery_size == '130X180':
    price_for_one = 190
    if 50 > joinery_count > 20:
        discount = 0.07
    elif joinery_count > 50:
        discount = 0.12

elif joinery_size == '200X300':
    price_for_one = 250
    if 50 > joinery_count > 25:
        discount = 0.09
    elif joinery_count > 50:
        discount = 0.14

if shipment_method == 'With delivery':
    delivery_price = 60
elif shipment_method == 'Without delivery':
    delivery_price = 0
total_price = price_for_one * joinery_count - ((price_for_one * joinery_count) * discount) + delivery_price

if joinery_count > 99:
    total_price -= (total_price * 0.04)
    print(f"{total_price:.2f} BGN")
elif joinery_count < 10:
    print('Invalid order')
elif joinery_count >= 10:
    print(f"{total_price:.2f} BGN")
