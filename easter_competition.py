
winner_points = 0

easter_breads = int(input())
for baker in range(easter_breads):
    baker_name = input()
    score_counter = 0
    command = input()
    while command != 'Stop':
        score = int(command)
        score_counter += score

        command = input()

    print(f"{baker_name} has {score_counter} points.")

    if score_counter > winner_points:
        winner_points = score_counter
        winner = baker_name
        print(f"{baker_name} is the new number 1!")

print(f"{winner} won competition with {winner_points} points!")


