training_fee = int(input())
sneakers_price = training_fee - 0.4 * training_fee
basketball_clothes = sneakers_price - 0.2 * sneakers_price
basketball_ball = basketball_clothes * 0.25
basketball_accessories = basketball_ball * 0.2
total = training_fee + sneakers_price + basketball_clothes \
        + basketball_ball + basketball_accessories
print(total)