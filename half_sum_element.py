from sys import maxsize
max_number = -maxsize
sum_number = 0
number_count = int(input())
for number in range(number_count):
    current_number = int(input())
    sum_number += current_number
    if current_number > max_number:
        max_number = current_number
if max_number == sum_number - max_number:
    print(f'Yes \nSum = {max_number}')
else:
    diff = abs(max_number - (sum_number - max_number))
    print(f'No \nDiff = {diff}')
