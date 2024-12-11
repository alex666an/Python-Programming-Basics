pastry_type = input()
pastry_count = float(input())
day = float(input())
if day <= 15:
    if pastry_type == 'Cake':
        price_for_one = 24
    elif pastry_type == 'Souffle':
        price_for_one = 6.66
    elif pastry_type == 'Baklava':
        price_for_one = 12.6
elif day > 15:
    if pastry_type == 'Cake':
        price_for_one = 28.7
    elif pastry_type == 'Souffle':
        price_for_one = 9.8
    elif pastry_type == 'Baklava':
        price_for_one = 16.98
total_sum = price_for_one * pastry_count
if day <= 22:
    if 100 <= total_sum <= 200:
        total_sum *= 0.85
    elif total_sum > 200:
        total_sum *= 0.75
if day <= 15:
    total_sum *= 0.9
print(f'{total_sum:.2f}')