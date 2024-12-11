deposit_amount = float(input())
deposit_lenght = int(input())
annual_interest_rate = float(input())
interest_rate = deposit_amount * annual_interest_rate / 100
month_interest_rate = interest_rate / 12
total_sum = deposit_amount + deposit_lenght * month_interest_rate
print(total_sum)
