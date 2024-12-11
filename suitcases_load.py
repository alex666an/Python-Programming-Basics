trunk_capacity = float(input())
suitcase_counter = 0
space_counter = 0
space_left = True

command = input()
while command != 'End':
    suitcase_counter += 1
    suitcase_volume = float(command)
    if suitcase_counter % 3 == 0:
        suitcase_volume *= 1.1

    if suitcase_volume > trunk_capacity:
        print("No more space!")
        space_left = False
        break
    elif trunk_capacity == suitcase_volume:
        print("No more space")
        space_left = False
        break

    trunk_capacity -= suitcase_volume
    command = input()

if space_left:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcase_counter} suitcases loaded.")

#50/100

