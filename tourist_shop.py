current_product_price = 0
counter = 0
budget = float(input())
product_name = input()
while product_name != 'Stop':
    product_price = float(input())
    counter += 1
    if counter % 3 == 0:
        product_price /= 2
    current_product_price += product_price

    if current_product_price > budget:
        break
    product_name = input()

difference = abs(budget - current_product_price)
if budget >= current_product_price:
    print(f"You bought {counter} products for {current_product_price:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {difference:.2f} leva!")
