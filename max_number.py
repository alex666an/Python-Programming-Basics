number = input()
max_number = -1000000000
while number != 'Stop':
    current_number = int(number)

    if current_number > max_number:
        max_number = current_number
    number = input()
print(max_number)
