dog_pack = int(input())
cat_pack = int(input())

dog_food_price = 2.5
cat_food_price = 4
dog_price_pack = dog_pack * dog_food_price
cat_price_pack = cat_pack * cat_food_price
total_price = dog_price_pack + cat_price_pack

print (f'{total_price} lv.')
