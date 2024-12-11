group1_counter = 0
group2_counter = 0
group3_counter = 0
food_needed = 0

cat_number = int(input())
for cats in range(cat_number):
    grams_eaten_per_cat = float(input())
    if 100 <= grams_eaten_per_cat < 200:
        group1_counter += 1
    elif 200 <= grams_eaten_per_cat < 300:
        group2_counter += 1
    elif 300 <= grams_eaten_per_cat < 400:
        group3_counter += 1
    food_needed += grams_eaten_per_cat
    food_needed_in_kg = food_needed / 1000
    price_for_food_per_day = food_needed_in_kg * 12.45


print(f"Group 1: {group1_counter} cats.")
print(f"Group 2: {group2_counter} cats.")
print(f"Group 3: {group3_counter} cats.")
print(f"Price for food per day: {price_for_food_per_day:.2f} lv.")


