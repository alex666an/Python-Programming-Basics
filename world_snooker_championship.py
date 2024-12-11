ticket_price = 0
tickets_total = 0
championship_progress = input()
ticket_type = input()
ticket_count = int(input())
trophy_photo = input()
if ticket_type == 'Standard':
    if championship_progress == 'Quarter final':
        ticket_price = 55.50
    elif championship_progress == 'Semi final':
        ticket_price = 75.88
    elif championship_progress == 'Final':
        ticket_price = 110.10
elif ticket_type == 'Premium':
    if championship_progress == 'Quarter final':
        ticket_price = 105.20
    elif championship_progress == 'Semi final':
        ticket_price = 125.22
    elif championship_progress == 'Final':
        ticket_price = 160.66
elif ticket_type == 'VIP':
    if championship_progress == 'Quarter final':
        ticket_price = 118.90
    elif championship_progress == 'Semi final':
        ticket_price = 300.40
    elif championship_progress == 'Final':
        ticket_price = 400
if trophy_photo == 'Y':
    trophy_price = ticket_count * 40
elif trophy_photo == 'N':
    trophy_price = 0
tickets_total = ticket_price * ticket_count
if 4000 >= tickets_total > 2500:
    tickets_total *= 0.9
    tickets_total += trophy_price
elif tickets_total > 4000:
    tickets_total *= 0.75

print(f'{tickets_total:.2f}')


