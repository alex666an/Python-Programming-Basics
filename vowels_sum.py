text = input()
sum = 0
for index in range(0,len(text)):
    if text[index] == 'a':
        sum += 1
    elif text[index] == 'e':
        sum += 2
    elif text[index] == 'i':
        sum += 3
    elif text[index] == 'o':
        sum += 4
    elif text[index] == 'u':
        sum += 5
print(sum)
