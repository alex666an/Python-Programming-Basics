first_player_points = 0
second_player_points = 0
game = ''
first_player_name = input()
second_player_name = input()
while game != 'End of game':
    first_player_card = input()
    if first_player_card == 'End of game':
        print(f"{first_player_name} has {first_player_points} points")
        print(f"{second_player_name} has {second_player_points} points")
        break

    second_player_card = input()

    if int(first_player_card) > int(second_player_card):
        first_player_points += int(first_player_card) - int(second_player_card)
    elif int(second_player_card) > int(first_player_card):
        second_player_points += int(second_player_card) - int(first_player_card)
    else:
        first_player_2card = int(input())
        second_player_2card = int(input())
        if first_player_2card > second_player_2card:
            print("Number wars!")
            print(f"{first_player_name} is winner with {first_player_points} points")

        else:
            print("Number wars!")
            print(f"{second_player_name} is winner with {second_player_points} points")
        break









