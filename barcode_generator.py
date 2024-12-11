first_number = int(input())
second_number = int(input())
for a in range(int(str(first_number)[0]), int(str(second_number)[0]) + 1):
    for b in range(int(str(first_number)[1]), int(str(second_number)[1]) + 1):
        for c in range(int(str(first_number)[2]), int(str(second_number)[2]) + 1):
            for d in range(int(str(first_number)[3]), int(str(second_number)[3]) + 1):
             if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                 print(f'{a}{b}{c}{d}', end=' ')


