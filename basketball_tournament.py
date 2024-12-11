win = 0
lost = 0
total_matches = 0
difference = 0


while True:
    name_of_tournament = input()
    game_counter = 0
    if name_of_tournament == 'End of tournaments':
        break
    number_of_matches = int(input())
    total_matches += number_of_matches
    for match in range(number_of_matches):
        game_counter += 1
        desi_points = int(input())
        opponent_points = int(input())
        if desi_points > opponent_points:
            difference = abs(desi_points - opponent_points)
            win += 1
            print(f"Game {game_counter} of tournament {name_of_tournament}: win with {difference} points.")
        elif desi_points < opponent_points:
            difference = abs(desi_points - opponent_points)
            lost += 1
            print(f"Game {game_counter} of tournament {name_of_tournament}: lost with {difference} points.")

percent_won_matches = win / total_matches * 100
percent_lost_matches = lost / total_matches * 100
print(f'{percent_won_matches:.2f}% matches win')
print(f'{percent_lost_matches:.2f}% matches lost')
