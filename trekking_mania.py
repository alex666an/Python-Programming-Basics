number_of_groups = int(input())
musalla_climbers = 0
mont_blanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0
for climbers in range(number_of_groups):
    number_of_people_in_group = int(input())
    if number_of_people_in_group <= 5:
        musalla_climbers += number_of_people_in_group
    elif number_of_people_in_group <= 12:
        mont_blanc_climbers += number_of_people_in_group
    elif number_of_people_in_group <= 25:
        kilimanjaro_climbers += number_of_people_in_group
    elif number_of_people_in_group <= 40:
        k2_climbers += number_of_people_in_group
    elif number_of_people_in_group >= 41:
        everest_climbers += number_of_people_in_group
    total_climbers += number_of_people_in_group
musalla_percentage = musalla_climbers / total_climbers * 100
mont_blanc_percentage = mont_blanc_climbers / total_climbers * 100
kilimanjaro_percentage = kilimanjaro_climbers / total_climbers * 100
k2_percentage = k2_climbers / total_climbers * 100
everest_percentage = everest_climbers / total_climbers * 100
print(f'{musalla_percentage:.2f}%')
print(f'{mont_blanc_percentage:.2f}%')
print(f'{kilimanjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')