scores = list(map(int, input("入力").split()))

score_sum = 0
for score in scores:
    score_sum = score_sum + score

result = int(score_sum) / len(scores)

print(result)
