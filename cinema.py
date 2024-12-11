projection_type = input()
rows = int(input())
columns = int(input())
price = 0
if projection_type == 'Premiere':
    price = rows * columns * 12
elif projection_type == 'Normal':
    price = rows * columns * 7.5
elif projection_type == 'Discount':
    price = rows * columns * 5
print(f'{price:.2f} leva')

