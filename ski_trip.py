days = int(input())
room_type = input()
score = input()
nights = days - 1
price = 0
if days < 10:
    if room_type == 'room for one person':
        price = nights * 18
    elif room_type == 'apartment':
        price = nights * 25
    elif room_type == 'president apartment':
        price = nights * 35
if 10 <= days <= 15:
    if room_type == 'room for one person':
        price = nights * 18
    if room_type == 'apartment':
        price = nights * 25 * 0.65
    if room_type == 'president apartment':
        price = nights * 35 * 0.5
if days > 15:
    if room_type == 'room for one person':
        price = nights * 18
    if room_type == 'apartment':
        price = nights * 25 * 0.5
    if room_type == 'president apartment':
        price = nights * 35 * 0.8
if score == 'positive':
    price *= 1.25
elif score == 'negative':
    price *= 0.9
print(f'{price:.2f}')










