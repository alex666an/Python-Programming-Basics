num = int(input())

for a in range(1, num + 1):
    print((num - a) * " ", end="")
    print('*', end="")
    print((a - 1) * " *", end="")
    print()
for b in range(num - 1, 0, - 1):
    print((num - b) * " ", end="")
    print('*', end="")
    print((b - 1) * " *", end="")
    print()

