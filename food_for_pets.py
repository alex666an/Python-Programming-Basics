number_of_days = int(input())
total_food = float(input())
biscuits = 0
total_food_eaten_in_a_day = 0
total_food_eaten_by_dog = 0
total_food_eaten_by_cat = 0
total_biscuits = 0
for food in range(1, number_of_days + 1):
    food_eaten_by_dog = int(input())
    total_food_eaten_by_dog += food_eaten_by_dog

    food_eaten_by_cat = int(input())
    total_food_eaten_by_cat += food_eaten_by_cat

    food_eaten_in_a_day = food_eaten_by_dog + food_eaten_by_cat

    if number_of_days % 3 == 0:
        biscuits = food_eaten_in_a_day * 0.1
        total_biscuits += biscuits

    total_food_eaten_in_a_day += food_eaten_in_a_day


percentage_total_food_eaten = total_food_eaten_in_a_day / total_food * 100
percentage_food_eaten_by_dog = total_food_eaten_by_dog / total_food_eaten_in_a_day * 100
percentage_food_eaten_by_cat = total_food_eaten_by_cat / total_food_eaten_in_a_day * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{percentage_total_food_eaten:.2f}% of the food has been eaten.")
print(f"{percentage_food_eaten_by_dog:.2f}% eaten from the dog.")
print(f"{percentage_food_eaten_by_cat:.2f}% eaten from the cat.")



