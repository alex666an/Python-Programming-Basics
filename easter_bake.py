import math
sugar_counter = 0
flour_counter = 0
max_sugar = 0
max_flour = 0
easter_breads = int(input())
for bake in range(easter_breads):
    used_sugar = int(input())
    sugar_counter += used_sugar
    used_flour = int(input())
    flour_counter += used_flour
    needed_sugar_pack = math.ceil(sugar_counter / 950)
    needed_flour_pack = math.ceil(flour_counter / 750)
    if used_sugar > max_sugar:
        max_sugar = used_sugar

    if used_flour > max_flour:
        max_flour = used_flour


print(f"Sugar: {needed_sugar_pack}")
print(f"Flour: {needed_flour_pack}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")