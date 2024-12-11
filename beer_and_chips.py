import math
name = input()
budget = float(input())
bottles = int(input())
chips_packet = int(input())
beer_price = 1.2 * bottles
chips_price_for_one_pack = beer_price * 0.45
chips_price = math.ceil(chips_price_for_one_pack * chips_packet)
total_sum = beer_price + chips_price
difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"{name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{name} needs {difference:.2f} more leva!")