strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())
raspberries_price = strawberry_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2
total_sum = strawberries_kg * strawberry_price + bananas_price * bananas_kg \
            + oranges_price * oranges_kg + raspberries_price * raspberries_kg
print(f'{total_sum:.2f}')