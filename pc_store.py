processor_in_dollars = float(input())
video_card_in_dollars = float(input())
ram_in_dollars = float(input())
number_of_ram = int(input())
percentage_discount = float(input())
processor_in_bgn = processor_in_dollars * 1.57
video_card_in_bgn = video_card_in_dollars * 1.57
ram_price_in_bgn = (number_of_ram * ram_in_dollars) * 1.57
processor_with_discount = processor_in_bgn - (processor_in_bgn * percentage_discount)
video_card_with_discount = video_card_in_bgn - (video_card_in_bgn * percentage_discount)
total = ram_price_in_bgn + processor_with_discount + video_card_with_discount
print(f"Money needed - {total:.2f} leva.")
