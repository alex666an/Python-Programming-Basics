player_name = input()
game = ''
points_left = 301
successful = 0
unsuccessful = 0
while True:
    type = input()
    if type == 'Retire':
        print(f'{player_name} retired after {unsuccessful} unsuccessful shots.')
        break
    points = int(input())
    if type == 'Single':
        points = points
        if points <= points_left:
            points_left -= points
            successful += 1
        else:
            unsuccessful += 1

    elif type == 'Double':
        points = (points * 2)
        if points <= points_left:
            points_left -= points
            successful += 1
        else:
            unsuccessful += 1
    elif type == 'Triple':
        points = (points * 3)
        if points <= points_left:
            points_left -= points
            successful += 1
        else:
            unsuccessful += 1
    if points_left == 0:
        print(f"{player_name} won the leg with {successful} shots.")
        break
        type = input()
        points = int(input())




