minutes_walking_per_day = int(input())
walks_per_day = int(input())
calories_consumed_per_day = int(input())
walking_time = minutes_walking_per_day * walks_per_day
burned_calories = walking_time * 5
if burned_calories >= calories_consumed_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")