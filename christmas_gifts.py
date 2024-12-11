kid_counter = 0
adult_counter = 0
toy_price = 0
sweater_price = 0

command = input()
while command != 'Christmas':
    years = int(command)
    if years <= 16:
        kid_counter += 1
        toy_price += 5
    elif years > 16:
        adult_counter += 1
        sweater_price += 15
    command = input()


print(f"Number of adults: {adult_counter}")
print(f"Number of kids: {kid_counter}")
print(f"Money for toys: {toy_price}")
print(f"Money for sweaters: {sweater_price}")