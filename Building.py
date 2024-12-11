floors = int(input())
rooms = int(input())
for floor in reversed(range(1,floors + 1)):
    if floor % 2 == 0:
        room_type = 'O'
    else:
        room_type = 'A'

    if floor == floors:
        room_type = 'L'

    for room in range(rooms):
        room_name = (f'{room_type}{floor}{room}')
        print(room_name, end=' ')
    print()



