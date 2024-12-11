chicken_meals = int(input())
fish_meals = int(input())
vegan_meals  = int(input())
chicken_price = 10.35
fish_price = 12.40
vegan_price = 8.15
main_course_price = chicken_meals * chicken_price \
                    + fish_meals * fish_price \
                    + vegan_meals * vegan_price
dessert_price = main_course_price / 5
delivery_price = 2.5
total_sum = main_course_price + dessert_price + delivery_price
print(total_sum)