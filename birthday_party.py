rent_of_hall = float(input())
cake_price = rent_of_hall * 0.2
drinks_price = cake_price * 0.55
animator_price = rent_of_hall / 3
budget = rent_of_hall + cake_price + drinks_price + animator_price
print(budget)