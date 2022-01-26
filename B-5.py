"""
スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
合計値
最大値
最小値
平均値
ただし、組み込み関数やライブラリは使わないこと(sum()やnp.mean()など)
1つの統計量につき、それ専用の関数を実装すること
実行例
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
"""


def goukei():
    score_sum = 0
    for score in scores:
        score_sum = score_sum + score
    return score_sum


# splitで文字列を区切り文字を分割しリスト化

def saidai():
    max_s = 0
    for score in scores:
        if max_s < score:
            max_s = score
    return max_s


scores = list(map(int, input("入力").split()))

print("合計値:" + str(goukei()))
print("最大値:" + str(saidai()))
