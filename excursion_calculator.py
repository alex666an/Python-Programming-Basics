price_per_person = 0
number_of_people = int(input())
season = input()
if season == 'spring':
    if number_of_people <= 5:
        price_per_person = 50
    elif number_of_people > 5:
        price_per_person = 48
elif season == 'summer':
    if number_of_people <= 5:
        price_per_person = 48.5
    elif number_of_people > 5:
        price_per_person = 45
elif season == 'autumn':
    if number_of_people <= 5:
        price_per_person = 60
    elif number_of_people > 5:
        price_per_person = 49.5
elif season == 'winter':
    if number_of_people <= 5:
        price_per_person = 86
    elif number_of_people > 5:
        price_per_person = 85
total_price = number_of_people * price_per_person
if season == 'summer':
    total = total_price - (total_price * 0.15)
elif season == 'winter':
    total = total_price + (total_price * 0.08)
else:
    total = total_price
print(f"{total:.2f} leva.")

