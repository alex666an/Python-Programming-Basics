number_of_locations = int(input())
for locations in range(number_of_locations):
    expected_average_gold_yield_per_day = float(input())
    number_of_days_dig_per_location = int(input())
    gold_yield_for_current_day_counter = 0
    for days in range(number_of_days_dig_per_location):
        gold_yield_for_current_day = float(input())
        gold_yield_for_current_day_counter += gold_yield_for_current_day
    average_yield_per_day = gold_yield_for_current_day_counter / number_of_days_dig_per_location
    difference = abs(average_yield_per_day - expected_average_gold_yield_per_day)
    if average_yield_per_day >= expected_average_gold_yield_per_day:
        print(f"Good job! Average gold per day: {average_yield_per_day:.2f}.")
    else:
        print(f"You need {difference:.2f} gold.")


