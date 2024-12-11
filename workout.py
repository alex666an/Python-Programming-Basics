km_totinitial_schedulel = 0
training_days = int(input())
km_in_first_day = float(input())
for _ in range(1, training_days + 1):
    current_rate = int(input())
    current_rate_percent = current_rate / 100
    per_day = (km_in_first_day * current_rate) + km_in_first_day
    km_in_first_day == per_day
    km_total += km_in_first_day
difference = abs(km_total - 1000)
if km_total >= 1000:
    print(f"You've done a great job running {difference:.2f} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {difference:.2f} more kilometers")





    



