counter = 0
unsuccessful_counter = 0
limit = 0
successful = True

record_height = int(input())
record = record_height - 30
while True:
    for _ in range(0,2):
        jump_height = int(input())
        counter += 1
        if jump_height > record:
            unsuccessful_counter = 0
            if record >= record_height:
                limit = record
                print(f"Tihomir succeeded, he jumped over {record}cm after {counter} jumps.")
                break
            record += 5
            break
        if jump_height <= record:
            unsuccessful_counter += 1
            if unsuccessful_counter == 3:
                print(f"Tihomir failed at {record}cm after {counter} jumps.")
                break
    if limit >= record_height:
        break
    if unsuccessful_counter == 3:
        break


