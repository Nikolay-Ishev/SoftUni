movie = input()
taken_seats_total = 0
standard_total = 0
kid_total = 0
student_total = 0
while movie != "Finish":
    taken_seats_movie = 0
    free_seats = int(input())
    while taken_seats_movie < free_seats:
        ticket_type = input()
        if ticket_type != "End":
            taken_seats_movie += 1
            taken_seats_total += 1
            if ticket_type == "standard":
                standard_total += 1
            elif ticket_type == "kid":
                kid_total += 1
            elif ticket_type == "student":
                student_total += 1
        else:
            break
    print(f"{movie} - {(taken_seats_movie / free_seats * 100):.2f}% full.")
    movie = input()
print(f"Total tickets: {taken_seats_total}")
print(f"{(student_total / taken_seats_total * 100):.2f}% student tickets.")
print(f"{(standard_total / taken_seats_total * 100):.2f}% standard tickets.")
print(f"{(kid_total / taken_seats_total * 100):.2f}% kids tickets.")





