tshirt_price = float(input())
money_for_prize = float(input())
shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (tshirt_price + shorts_price) * 2
total_sum = tshirt_price + shorts_price + socks_price + shoes_price
total_sum_with_discount = total_sum - (total_sum * 0.15)
difference = abs(money_for_prize - total_sum_with_discount)
if total_sum_with_discount >= money_for_prize:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum_with_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")