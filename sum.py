def calculate_scores(scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average
scores_list = [85, 90, 78, 92, 88]
total, avg = calculate_scores(scores_list)
print("Scores:", scores_list)
print("Sum of scores:", total)
print("Average of scores:",avg)