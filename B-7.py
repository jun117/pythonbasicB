def goukei(scores):
    score_sum = 0
    for score in scores:
        score_sum = score_sum + score
    return score_sum


def saidai():


scores = list(map(int, input("入力").split()))

print("合計値:" + str(goukei(scores)))
