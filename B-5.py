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
# result=input('データを入力してください>').split(",")

# print(result)

# i = list(map(int, input("入力待ち画面に出力するメッセージ").split(",")))
# print(i) # i変数の中身を出力

# 例)入力：s_1 s_2

# -*- coding: utf-8 -*-

scores = list(map(int, input("入力").split()))

score_sum = 0

for score in scores:
    score_sum = score_sum + score

print(f'10人の点数の合計は、{score_sum}')

# 入力値：1,2,3
# 実行結果：['1', '2', '3']
