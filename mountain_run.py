starting_record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_climbing_1_meter_in_seconds = float(input())
total_climbing_distance = distance_in_meters * time_for_climbing_1_meter_in_seconds
delay = (distance_in_meters // 50) * 30
new_record = total_climbing_distance + delay
difference = abs(new_record - starting_record_in_seconds)
if new_record < starting_record_in_seconds:
    print(f"Yes! The new record is {new_record:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")