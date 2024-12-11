lenght = int(input())
width = int(input())
height = int(input())
percentage = float(input())
aquarium_volume_in_cm = lenght * width * height
aquarium_volume_in_litres = aquarium_volume_in_cm / 1000
space_filled_with_water = aquarium_volume_in_litres * (1 - percentage / 100)
print(space_filled_with_water)