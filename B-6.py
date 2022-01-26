def goukei():
    score_sum = 0
    for score in scores:
        score_sum = score_sum + score
    return score_sum


# splitで文字列を区切り文字を分割しリスト化
scores = list(map(int, input("入力").split()))

print("合計値:" + str(goukei()))


def saidai():
    max_s = 0
    for score in scores:
        if max_s < score:
            max_s = score
    return max_s


print(saidai())


def saisyo():
    min_s = scores[0]
    for score in scores:
        if score < min_s:
            min_s = score
    return min_s


print(saisyo())

score_sum = 0
for score in scores:
    score_sum = score_sum + score
    result = score_sum / (len(score) - 1)
print(result)
