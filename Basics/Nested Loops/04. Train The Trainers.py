n = int(input())
presentation = input()
all_scores = 0
presentation_n = 0
while presentation != "Finish":
    score_sum = 0
    for scores in range(n):
        score = float(input())
        score_sum += score
    print(f"{presentation} - {(score_sum / n):.2f}.")
    all_scores += (score_sum / n)
    presentation_n += 1
    presentation = input()
print(f"Student's final assessment is {(all_scores / presentation_n):.2f}.")



