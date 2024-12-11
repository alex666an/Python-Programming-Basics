page_count = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())
time_needed_for_reading = page_count / pages_per_hour
days_needed_for_reading = time_needed_for_reading / days_for_reading
print(int(days_needed_for_reading))