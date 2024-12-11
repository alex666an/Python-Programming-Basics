red_egg_counter = 0
orange_egg_counter = 0
blue_egg_counter = 0
green_egg_counter = 0

number_of_eggs = int(input())
for eggs in range(number_of_eggs):
    egg_colour = input()
    if egg_colour == 'red':
        red_egg_counter += 1
    elif egg_colour == 'orange':
        orange_egg_counter += 1
    elif egg_colour == 'blue':
        blue_egg_counter += 1
    elif egg_colour == 'green':
        green_egg_counter += 1

    max_eggs_colour = max(red_egg_counter, orange_egg_counter, blue_egg_counter, green_egg_counter)
    if max_eggs_colour == red_egg_counter:
        colour = 'red'
    elif max_eggs_colour == orange_egg_counter:
        colour = 'orange'
    elif max_eggs_colour == blue_egg_counter:
        colour = 'blue'
    elif max_eggs_colour == green_egg_counter:
        colour = 'green'
print(f"Red eggs: {red_egg_counter}")
print(f"Orange eggs: {orange_egg_counter}")
print(f"Blue eggs: {blue_egg_counter}")
print(f"Green eggs: {green_egg_counter}")
print(f"Max eggs: {max_eggs_colour} -> {colour}")


