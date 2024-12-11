month = input()
nights = int(input())
studio_price = 0
apartment_price = 0
if month == 'May' or month == 'October':
    if 14 >= nights > 7:
        studio_price = nights * 50 * 0.95
    elif nights > 14:
        studio_price = nights * 50 * 0.7
    else:
        studio_price = nights * 50
    if nights > 14:
        apartment_price = nights * 65 * 0.9
    else:
        apartment_price = nights * 65
elif month == 'June' or month == 'September':
    if 14 >= nights > 7:
        studio_price = nights * 75.2 * 0.95
    elif nights > 14:
        studio_price = nights * 75.2 * 0.7
    else:
        studio_price = nights * 75.2
    if nights > 14:
        apartment_price = nights * 68.7 * 0.9
    else:
        apartment_price = nights * 68.7
elif month == 'July' or month == 'August':
    studio_price = nights * 76
    if nights > 14:
        apartment_price = nights * 77 * 0.9
    else:
        apartment_price = nights * 77
print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")


