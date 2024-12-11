from sys import maxsize

best_player = ""
winner_goals = -maxsize
hat_trick = False
goals = 0

while True:
    football_player_name = input()

    if football_player_name == "END":
        break

    goals = int(input())


    if goals > winner_goals:
        winner_goals = goals
        best_player = football_player_name
    if goals >= 3:
        hat_trick = True
    if goals >= 10:
        break


print(f"{best_player} is the best player!")

if hat_trick:
    print(f"He has scored {goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals} goals.")



