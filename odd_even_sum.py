number_count = int(input())
even_sum = 0
odd_sum = 0
for num in range(1,number_count + 1):
    current_number = int(input())
    if num % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number
if even_sum == odd_sum:
        print('Yes')
        print(f'Sum = {even_sum}')
else:
        difference = abs(even_sum - odd_sum)
        print('No')
        print(f'Diff = {difference}')

