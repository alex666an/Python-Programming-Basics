student_tickets = 0
standard_tickets = 0
kid_tickets = 0
name_of_movie = input()
while name_of_movie != 'Finish':
    free_seats = int(input())
    sold_tickets = 0
    for ticket in range(free_seats):
        current_ticket = input()
        if current_ticket == 'End':
            break
        elif current_ticket == 'student':
            student_tickets += 1
        elif current_ticket == 'standard':
            standard_tickets += 1
        elif current_ticket == 'kid':
            kid_tickets += 1
        sold_tickets += 1
    percent_full_hall = sold_tickets / free_seats * 100
    print(f"{name_of_movie} - {percent_full_hall:.2f}% full.")
    name_of_movie = input()
total_sold_tickets = standard_tickets + student_tickets + kid_tickets
percentage_of_student_tickets = student_tickets / total_sold_tickets * 100
percentage_of_standard_tickets = standard_tickets / total_sold_tickets * 100
percentage_of_kid_tickets = kid_tickets/ total_sold_tickets * 100
print(f"Total tickets: {total_sold_tickets}")
print(f"{percentage_of_student_tickets:.2f}% student tickets.")
print(f"{percentage_of_standard_tickets:.2f}% standard tickets.")
print(f"{percentage_of_kid_tickets:.2f}% kids tickets.")




