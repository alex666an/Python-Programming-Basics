day_counter = 0
hour_counter = 0
parking_price = 0
current_day_price = 0
total_price = 0

number_of_days = int(input())
hours_per_day = int(input())
for day in range(1, number_of_days + 1):
    current_day_price = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_price = 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            parking_price = 1.25
        else:
            parking_price = 1
        current_day_price += parking_price

    total_price += current_day_price

    print(f"Day: {day} - {current_day_price:.2f} leva")
print(f"Total: {total_price:.2f} leva")

