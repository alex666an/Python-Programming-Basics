n = int(input())
combination_found = False
for a in range(1, 10):
    for b in range(9, a, -1):
        for c in range(10):
            for d in range(9, c, -1):
                sum = a + b + c + d
                product = a * b * c * d
                if sum == product and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    flag = True
                    break
                if product // sum == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    combination_found = True
                    break
            if combination_found:
                break
        if combination_found:
            break
    if combination_found:
        break
if not combination_found:
    print("Nothing found")
