movie_budget = float(input())
actor_count = int(input())
clothing_price_for_one_actor = float(input())
clothing_total_price = actor_count * clothing_price_for_one_actor
decor = movie_budget * 0.1
if actor_count > 150:
    clothing_total_price *= 0.9
money_needed = clothing_total_price + decor
difference = abs(money_needed - movie_budget)
if money_needed > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")