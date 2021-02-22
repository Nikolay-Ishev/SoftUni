bad_scores = int(input())
title = input()
score_track = 0
bad_scores_track = 0
average_score = 0
title_save = "Enough"
while title != "Enough":
    score = int(input())
    title_save = title
    if score <= 4:
            bad_scores_track += 1
    if bad_scores_track >= bad_scores:
        print(f"You need a break, {bad_scores_track} poor grades.")
        break
    score_track += 1
    average_score += score
    title = input()
if title == "Enough":
    print(f"Average score: {(average_score / score_track):.2f}")
    print(f"Number of problems: {score_track}")
    print(f"Last problem: {title_save}")





