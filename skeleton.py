record = int(input())
seconds_control = int(input())
chute_length = float(input())
seconds_needed_for_100_meters = int(input())
record_in_seconds = record * 60 + seconds_control
delay = chute_length / 120
delay_seconds = delay * 2.5
time_of_marin = (chute_length / 100) * seconds_needed_for_100_meters - delay_seconds
difference = abs(time_of_marin - record_in_seconds)
if time_of_marin <= record_in_seconds:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_of_marin:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")

