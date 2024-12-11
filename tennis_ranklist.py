number_of_tournaments = int(input())
entry_points = int(input())
total_points = 0
tournaments_won = 0
for tournaments in range(number_of_tournaments):
    tournament_result = input()
    if tournament_result == 'W':
        total_points += 2000
        tournaments_won += 1
    elif tournament_result == 'F':
        total_points += 1200
    elif tournament_result == 'SF':
        total_points += 720
average_points = total_points // number_of_tournaments
total_points += entry_points
percentage_of_won_tournaments = tournaments_won / number_of_tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f'{percentage_of_won_tournaments:.2f}%')
