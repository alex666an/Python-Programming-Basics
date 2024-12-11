name_of_actor = input()
academy_points = float(input())
number_of_judges = int(input())
total_points = academy_points
for grade in range(number_of_judges):
    judge_name = input()
    points_from_judge = float(input())
    current_points = len(judge_name) * points_from_judge / 2
    total_points += current_points
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.5 - total_points
    print(f"Sorry, {name_of_actor} you need {difference:.1f} more!")




