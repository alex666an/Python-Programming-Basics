nylon_quantity = int(input())
paint_quantity = int(input())
thinner_quantity = int(input())
work_hours = int(input())
nylon_price = 1.5
paint_price = 14.5
thinner_price = 5
bags_price = 0.40
price_of_materials = nylon_price * (nylon_quantity + 2) \
                     + paint_price * (paint_quantity * 1.1) \
                     + thinner_price * thinner_quantity + bags_price
workers_payment = price_of_materials * 0.30 * work_hours
total = price_of_materials + workers_payment
print(total)