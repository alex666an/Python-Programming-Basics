egg_quantity = 0
sold_eggs = 0
egg_quantity = int(input())
command = input()
while command != 'Close':
    starting_eggs = int(input())
    if command == 'Buy':
        if egg_quantity >= starting_eggs:
            sold_eggs += starting_eggs
            egg_quantity -= starting_eggs
        else:
            break
    elif command == 'Fill':
        egg_quantity += starting_eggs

    command = input()

if command == 'Close':
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
else:
    print("Not enough eggs in store!")
    print(f"You can buy only {egg_quantity}.")






