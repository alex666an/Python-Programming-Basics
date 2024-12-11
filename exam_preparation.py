number_of_bad_grades_allowed = int(input())
average_grade = 0
total_problems_solved = 0
bad_grades_counter = 0
last_problem_name = ''
has_failed = False
current_problem = input()
while current_problem != 'Enough':
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == number_of_bad_grades_allowed:
            has_failed = True
            break
    average_grade += current_grade
    total_problems_solved += 1
    last_problem_name = current_problem
    current_problem = input()
if has_failed:
    print(f"You need a break, {bad_grades_counter} poor grades.")
else:
    average_grade /= total_problems_solved
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {total_problems_solved}")
    print(f"Last problem: {last_problem_name}")