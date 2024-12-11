current_sum = 0
target_reached = False
daily_target = int(input())
command = input()
while command != 'closed':
    if command == 'haircut':
        haircut_type = input()
        if haircut_type == 'mens':
            current_sum += 15
        elif haircut_type == 'ladies':
            current_sum += 20
        elif haircut_type == 'kids':
            current_sum += 10
    elif command == 'color':
        coloring_type = input()
        if coloring_type == 'touch up':
            current_sum += 20
        elif coloring_type == 'full color':
            current_sum += 30
    if current_sum >= daily_target:
        target_reached = True
        break

    command = input()

difference = abs(current_sum - daily_target)
if target_reached:
    print(f'You have reached your target for the day!')
    print(f"Earned money: {current_sum}lv.")
else:
    print(f"Target not reached! You need {difference}lv. more.")
    print(f"Earned money: {current_sum}lv.")
