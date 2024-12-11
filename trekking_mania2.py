number_of_groups = int(input())
mussala_counter = 0
monblan_counter = 0
kilimanjaro_counter = 0
k2_counter = 0
everest_counter  = 0
all_people = 0
for climbers in range(number_of_groups):
    number_of_people_in_current_group = int(input())
    if number_of_people_in_current_group <= 5:
        mussala_counter += number_of_people_in_current_group
    elif number_of_people_in_current_group <= 12:
        monblan_counter += number_of_people_in_current_group
    elif number_of_people_in_current_group <= 25:
        kilimanjaro_counter += number_of_people_in_current_group
    elif number_of_people_in_current_group <= 40:
        k2_counter += number_of_people_in_current_group
    elif number_of_people_in_current_group >= 41:
        everest_counter += number_of_people_in_current_group
    all_people = mussala_counter + monblan_counter + kilimanjaro_counter + k2_counter + everest_counter
mussala_percentage = mussala_counter / all_people * 100
monblan_percentage = monblan_counter / all_people * 100
kilimanjaro_percentage = kilimanjaro_counter / all_people * 100
k2_percentage = k2_counter / all_people * 100
everest_percentage = everest_counter / all_people * 100
print(f'{mussala_percentage:.2f}%')
print(f'{monblan_percentage:.2f}%')
print(f'{kilimanjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')

