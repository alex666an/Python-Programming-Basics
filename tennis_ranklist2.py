import math
points = 0
win_counter = 0
number_of_tournaments = int(input())
starting_points = int(input())
points += starting_points
for tournament in range(number_of_tournaments):
    tournament_progress = input()

    if tournament_progress == 'W':
        points += 2000
        win_counter += 1
    elif tournament_progress == 'F':
        points += 1200
    elif tournament_progress == 'SF':
        points += 720
average_points = (points - starting_points) / number_of_tournaments
percentage_won = (win_counter / number_of_tournaments) * 100
print(f"Final points: {points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percentage_won:.2f}%")


