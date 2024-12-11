bitcoin_count = int(input())
chinese_yuan_count = float(input())
commission = float(input())
bitcoin_in_bgn = bitcoin_count * 1168
chinese_yuan_in_dollars = chinese_yuan_count * 0.15
chinese_yuan_in_bgn = chinese_yuan_in_dollars * 1.76
total_sum_without_commission = (bitcoin_in_bgn + chinese_yuan_in_bgn) / 1.95
commission_value = commission / 100 * total_sum_without_commission
total_sum = total_sum_without_commission - commission_value
print(f'{total_sum:.2f}')