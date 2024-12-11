width = int(input())
lenght = int(input())
height = int(input())
free_space = True
total_volume = width * lenght * height
command = input()
while command != 'Done':
    current_number_of_boxes = int(command)
    total_volume -= current_number_of_boxes
    if total_volume <= 0:
        free_space = False
        break
    command = input()
if free_space:
    print(f"{total_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")






