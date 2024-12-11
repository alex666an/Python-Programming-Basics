import math
tennis_racket_price = float(input())
tennis_racket_count = int(input())
shoes_count = int(input())
shoes_price = tennis_racket_price / 6
tennis_racket_total = tennis_racket_count * tennis_racket_price
shoes_total = shoes_price * shoes_count
racket_and_shoes = shoes_total + tennis_racket_total
other_equipment = racket_and_shoes / 5
total_sum = racket_and_shoes + other_equipment
paid_by_djokovic = total_sum / 8
paid_by_sponsors = total_sum * 7 / 8
print(f"Price to be paid by Djokovic {math.floor(paid_by_djokovic)}")
print(f"Price to be paid by sponsors {math.ceil(paid_by_sponsors)}")
