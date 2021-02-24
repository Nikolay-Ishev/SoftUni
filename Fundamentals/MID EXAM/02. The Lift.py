# Programming Fundamentals Mid Exam Retake 12 August 2020
# Problem 2. The Lift


people = int(input())
lift = input().split()
int_lift = [int(x) for x in lift]
for index in range(len(int_lift)):
    while int_lift[index] < 4 and people > 0:
        int_lift[index] += 1
        people -= 1
    # for cabin in int_lift:
#     while cabin < 4 and people > 0:
#         cabin += 1
#         people -= 1
lift_str = [str(x) for x in int_lift]
if people == 0 and int_lift.count(4) != len(int_lift):
    print("The lift has empty spots!")
elif people > 0 and int_lift.count(4) == len(lift):
    print(f"There isn't enough space! {people} people in a queue!")
print(" ".join(lift_str))
