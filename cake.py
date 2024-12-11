cake_width = int(input())
cake_lenght = int(input())
cake_left = 0
cake_size = cake_width * cake_lenght
there_is_cake_left = True
command = input()
while command != 'STOP':
    piece = int(command)
    cake_size -= piece
    if cake_size <= 0:
        there_is_cake_left = False
        break
    command = input()
if there_is_cake_left:
    print(f"{cake_size} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")
    

