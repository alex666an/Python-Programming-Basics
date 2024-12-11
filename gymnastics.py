difficulty = 0
execution = 0
country = input()
object = input()
if object == 'ribbon':
    if country == 'Russia':
        difficulty = 9.100
        execution = 9.400
    elif country == 'Bulgaria':
        difficulty = 9.600
        execution = 9.400
    elif country == 'Italy':
        difficulty = 9.200
        execution = 9.500
elif object == 'hoop':
    if country == 'Russia':
        difficulty = 9.300
        execution = 9.800
    elif country == 'Bulgaria':
        difficulty = 9.550
        execution = 9.750
    elif country == 'Italy':
        difficulty = 9.450
        execution = 9.350
elif object == 'rope':
    if country == 'Russia':
        difficulty = 9.600
        execution = 9.000
    elif country == 'Bulgaria':
        difficulty = 9.500
        execution = 9.400
    elif country == 'Italy':
        difficulty = 9.700
        execution = 9.150
total_score = difficulty + execution
percent_left = (20 - total_score) / 20 * 100
print(f"The team of {country} get {total_score:.3f} on {object}.")
print(f"{percent_left:.2f}%")

