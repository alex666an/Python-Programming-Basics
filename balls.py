score = 0
red_ball_counter = 0
orange_ball_counter = 0
yellow_ball_counter = 0
white_ball_counter = 0
black_ball_counter = 0
other_ball_counter = 0
ball_count = int(input())
for balls in range(ball_count):
    ball_color = input()
    if ball_color == 'red':
        score += 5
        red_ball_counter += 1
    elif ball_color == 'orange':
        score += 10
        orange_ball_counter += 1
    elif ball_color == 'yellow':
        score += 15
        yellow_ball_counter += 1
    elif ball_color == 'white':
        score += 20
        white_ball_counter += 1
    elif ball_color == 'black':
        score //= 2
        black_ball_counter += 1
    else:
        other_ball_counter += 1

print(f"Total points: {score}")
print(f"Red balls: {red_ball_counter}")
print(f"Orange balls: {orange_ball_counter}")
print(f"Yellow balls: {yellow_ball_counter}")
print(f"White balls: {white_ball_counter}")
print(f"Other colors picked: {other_ball_counter}")
print(f"Divides from black balls: {black_ball_counter}")


