basket_price = 1.5
wreath_price = 3.8
chocolate_bunny_price = 7
total_per_client = 0
number_of_clients = int(input())
for purchase in range(number_of_clients):
    counter = 0
    total = 0
    while True:

        command = input()
        if command == 'basket':
            total += basket_price
            counter += 1
        elif command == 'wreath':
            total += wreath_price
            counter += 1
        elif command == 'chocolate bunny':
            total += chocolate_bunny_price
            counter += 1
        elif command == 'Finish':
            if counter % 2 == 0:
                total *= 0.8
            total_per_client += total
            print(f"You purchased {counter} items for {total:.2f} leva.")
            break


average_bill = total_per_client / number_of_clients
print(f"Average bill per client is: {average_bill:.2f} leva.")



