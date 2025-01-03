needed_money = float(input())
available_money = float(input())
days_counter = 0
spend_counter = 0
total_days_counter = 0
spending_too_many_days_in_a_row = False
while available_money < needed_money:
    action = input()
    current_sum = float(input())
    total_days_counter += 1
    if action == 'spend':
        spend_counter += 1
        if spend_counter == 5:
            spending_too_many_days_in_a_row = True
            break
        available_money -= current_sum
        if available_money < 0:
            available_money = 0
    elif action == 'save':
        available_money += current_sum
        spend_counter = 0
if spending_too_many_days_in_a_row:
    print("You can't save the money.")
    print(total_days_counter)
else:
    print(f"You saved the money for {total_days_counter} days.")
