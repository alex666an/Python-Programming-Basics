fruit_type = input()
set_size = input()
set_count = int(input())
price_per_set = 0
if fruit_type == 'Watermelon' and set_size == 'small':
    price_per_set = 2 * 56
elif fruit_type == 'Watermelon' and set_size == 'big':
    price_per_set = 5 * 28.7
elif fruit_type == 'Mango' and set_size == 'small':
    price_per_set = 2 * 36.66
elif fruit_type == 'Mango' and set_size == 'big':
    price_per_set = 5 * 19.6
elif fruit_type == 'Pineapple' and set_size == 'small':
    price_per_set = 2 * 42.1
elif fruit_type == 'Pineapple' and set_size == 'big':
    price_per_set = 5 * 24.8
elif fruit_type == 'Raspberry' and set_size == 'small':
    price_per_set = 2 * 20
elif fruit_type == 'Raspberry' and set_size == 'big':
    price_per_set = 5 * 15.2
total_fruit_price = set_count * price_per_set
if 1000 >= total_fruit_price >= 400:
    total_fruit_price *= 0.85
elif total_fruit_price > 1000:
    total_fruit_price *= 0.5
print(f"{total_fruit_price:.2f} lv.")




