import math
series_name = str(input())
episode_lenght = int(input())
break_lenght = int(input())
lunch_break =  break_lenght * 0.125
rest_time = break_lenght * 0.25
time_left_for_series = break_lenght - (lunch_break + rest_time)
difference = abs(time_left_for_series - episode_lenght)
difference = math.ceil(difference)
if time_left_for_series >= episode_lenght:
    print(f"You have enough time to watch {series_name} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {difference} more minutes.")