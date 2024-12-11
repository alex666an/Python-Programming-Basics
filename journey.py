budget = float(input())
season = input()
budget_used = 0
destination = ''
vacation_type = ''
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation_type = 'Camp'
        budget_used = budget * 0.3
    elif season == 'winter':
        vacation_type = 'Hotel'
        budget_used = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vacation_type = 'Camp'
        budget_used = budget * 0.4
    elif season == 'winter':
        vacation_type = 'Hotel'
        budget_used = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    vacation_type = 'Hotel'
    budget_used = budget * 0.9
print(f'Somewhere in {destination}')
print(f'{vacation_type} - {budget_used:.2f}')


