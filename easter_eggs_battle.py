eggs_of_first_player = int(input())
eggs_of_second_player = int(input())
command = input()
while command != 'End':
    if command == 'one':
        eggs_of_second_player -= 1
    elif command == 'two':
        eggs_of_first_player -= 1
    if eggs_of_first_player == 0:
        print(f"Player one is out of eggs. Player two has {eggs_of_second_player} eggs left.")
        break
    elif eggs_of_second_player == 0:
        print(f"Player two is out of eggs. Player one has {eggs_of_first_player} eggs left.")

    command = input()
if eggs_of_first_player > 0 and eggs_of_second_player > 0:
    print(f"Player one has {eggs_of_first_player} eggs left.")
    print(f"Player two has {eggs_of_second_player} eggs left.")











