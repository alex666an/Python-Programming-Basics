budget = float(input())
litres_of_fuel = float(input())
day_of_week = input()
fuel = litres_of_fuel * 2.1
tour_guide = 100
total = tour_guide + fuel
if day_of_week == 'Saturday':
    total *= 0.9
elif day_of_week == 'Sunday':
    total *= 0.8
difference = abs(budget - total)
if budget >= total:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")
