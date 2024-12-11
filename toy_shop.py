puzzle_price = 2.6
doll_price = 3
teddy_price = 4.1
minion_price = 8.2
truck_price = 2
vacation_price = float(input())
puzzles_quantity = int(input())
dolls_quantity = int(input())
teddies_quantity = int(input())
minions_quantity = int(input())
trucks_quantity = int(input())
puzzles = puzzles_quantity * puzzle_price
dolls = dolls_quantity * doll_price
teddies = teddies_quantity * teddy_price
minions = minions_quantity * minion_price
trucks = trucks_quantity * truck_price
total_earnings = puzzles + dolls + teddies + minions + trucks
total_quantity = puzzles_quantity * dolls_quantity \
                 + teddies_quantity + minions_quantity \
                 + trucks_quantity
if total_quantity >= 50:
    total_earnings *= 0.75
total_earnings *= 0.90
difference = abs(total_earnings - vacation_price)
if total_earnings >= vacation_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")



