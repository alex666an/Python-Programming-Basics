dogfood_counter = 0
difference = 0
bought_dog_food = int(input())
bought_dog_food_in_grams = bought_dog_food * 1000
command = input()
while command != 'Adopted':
    dogfood_eaten_per_meal = int(command)
    dogfood_counter += dogfood_eaten_per_meal
    command = input()
    difference = abs(dogfood_counter - bought_dog_food_in_grams)
if dogfood_counter < bought_dog_food_in_grams:
    print(f"Food is not enough. You need {difference} grams more.")
else:
    print(f"Food is enough! Leftovers: {difference} grams.")


