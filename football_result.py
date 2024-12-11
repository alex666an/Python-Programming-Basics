win = 0
lost = 0
draw = 0

for r in range(3):
    result = input()
    if int(result[0]) > int(result[2]):
        win += 1

    elif int(result[0]) < int(result[2]):
        lost += 1

    elif int(result[0]) == int(result[2]):
        draw += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draw}")

