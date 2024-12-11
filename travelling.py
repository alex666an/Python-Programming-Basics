while True:
    destination = input()
    if destination == 'End':
        break
    needed_money = float(input())
    saved_money = 0
    enough_money = False
    while saved_money < needed_money:
        current_money = float(input())
        saved_money += current_money
        if saved_money >= needed_money:
            enough_money = True
            break
    if enough_money:
        print(f'Going to {destination}!')



