number = input()
min_number = 1000000000
while number != 'Stop':
    current_number = int(number)

    if current_number < min_number:
        min_number = current_number
    number = input()
print(min_number)