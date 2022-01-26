"""
N面サイコロをM回振ったときの結果を表示してください
N, M は正の整数とします
N, M はユーザーからの入力を利用すること

サイコロの面の数は?: 8
何回振りますか?: 20
[6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]


# サイコロの1面の場合　1
# サイコロ面2　　　1　2
　サイコロの面3　　1　2　3

サイコロの面　4　1234
サイコロの面　5　12345
"""


def square():
    import random

    r = random.choice(range(1, int(number1) + 1))
    return (r)


number1 = input('サイコロの面数は？：')
number2 = input('何回振りますか？：')
l = []
for num in range(int(number2)):
    l.append(square())
    # この場合forの後ろの変数はどういう意味があるのでしょか？下のprintを繰り返させるだけすか？

print(l)
