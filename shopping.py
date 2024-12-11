budget = float(input())
videocard_count = int(input())
processor_count = int(input())
ram_memory_count = int(input())
videocard_price = 250
videocard_total = videocard_count * videocard_price
processor_price = videocard_total * 0.35
processor_total = processor_count * processor_price
ram_memory_price = videocard_total * 0.1
ram_memory_total = ram_memory_count * ram_memory_price
total_sum = videocard_total + processor_total + ram_memory_total
if videocard_count > processor_count:
    total_sum *= 0.85
difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")