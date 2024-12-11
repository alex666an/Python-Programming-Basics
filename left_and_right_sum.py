n = int(input())
left_sum = 0
right_sum = 0
difference = 0
for i in range(n):
    left_sum = left_sum + int(input())
for i in range(n):
    right_sum = right_sum + int(input())
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    difference = abs(right_sum - left_sum)
    print(f'No, diff = {difference}')



