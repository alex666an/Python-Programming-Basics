first_number = int(input())
second_number = int(input())
for number in range(first_number,second_number + 1):
    even_digit_sum = 0
    odd_digit_sum = 0
    number_as_str = str(number)
    for index in range (0,len(number_as_str)):
        for index, digit in enumerate(number_as_str):
            if index % 2 == 0:
                even_digit_sum += int(digit)
            else:
                odd_digit_sum += int(digit)
    if even_digit_sum == odd_digit_sum:
        print(number, end=" ")


