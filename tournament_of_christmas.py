number_of_days = int(input())

won_days = 0
lost_days = 0
days_won = 0
total_money = 0

for days in range(number_of_days):
    money_counter = 0
    games_won = 0
    games_lost = 0
    sport = input()
    while sport != 'Finish':
        result = input()
        if result == 'win':
            money_counter += 20
            games_won += 1
        elif result == 'lose':
            games_lost += 1

        sport = input()

    if games_won > games_lost:
        money_counter *= 1.1
        days_won += 1
    total_money += money_counter

if days_won > number_of_days // 2:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")