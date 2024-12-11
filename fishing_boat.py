budget = int(input())
season = input()
number_of_fishermen = int(input())
rent_total = 0
if season == 'Spring':
    if number_of_fishermen <= 6:
        rent_total = 3000 * 0.9
    elif number_of_fishermen <= 11:
        rent_total = 3000 * 0.85
    elif number_of_fishermen >= 12:
        rent_total = 3000 * 0.75
    else:
        rent_total = 3000
elif season == 'Summer' or season == 'Autumn':
    if number_of_fishermen <= 6:
        rent_total = 4200 * 0.9
    elif number_of_fishermen <= 11:
        rent_total = 4200 * 0.85
    elif number_of_fishermen >= 12:
        rent_total = 4200 * 0.75
    else:
        rent_total = 4200
elif season == 'Winter':
    if number_of_fishermen <= 6:
        rent_total = 2600 * 0.9
    elif number_of_fishermen <= 11:
        rent_total = 2600 * 0.85
    elif number_of_fishermen >= 12:
        rent_total = 2600 * 0.75
    else:
        rent_total = 2600
if number_of_fishermen % 2 == 0 and season != 'Autumn':
    rent_total *= 0.95
difference = abs(budget - rent_total)
if budget >= rent_total:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget < rent_total:
    print(f"Not enough money! You need {difference:.2f} leva.")
