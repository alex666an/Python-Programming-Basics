total_payments = 0
while True:
    payment = input()

    if payment == 'NoMoreMoney':
        break

    current_sum = float(payment)

    if current_sum >= 0:
        total_payments += current_sum
        print(f'Increase: {current_sum:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {total_payments:.2f}')

