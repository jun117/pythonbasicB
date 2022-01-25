def score_all():
    scores = list(map(int, input("入力").split()))
    score_sum = 0
    for score in scores:
        score_sum = score_sum + score


print(f'10人の点数の合計は、{score_all}')
