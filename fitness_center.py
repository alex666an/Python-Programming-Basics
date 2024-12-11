work_out_counter = 0
protein_counter = 0
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

number_of_visitors = int(input())
for fitness in range (number_of_visitors):
    fitness_action = input()
    if fitness_action == 'Back':
        back += 1
        work_out_counter += 1
    elif fitness_action == 'Chest':
        chest += 1
        work_out_counter += 1
    elif fitness_action == 'Legs':
        legs += 1
        work_out_counter += 1
    elif fitness_action == 'Abs':
        abs += 1
        work_out_counter += 1
    elif fitness_action == 'Protein shake':
        protein_shake += 1
        protein_counter += 1
    elif fitness_action == 'Protein bar':
        protein_bar += 1
        protein_counter += 1

percentage_working_out = work_out_counter / number_of_visitors * 100
percentage_buying_protein = protein_counter / number_of_visitors * 100
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{percentage_working_out:.2f}% - work out")
print(f"{percentage_buying_protein:.2f}% - protein")


