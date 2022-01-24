number1 = input('行数を入力してください：')
number2 = input('列数を入力してください：')

for count1 in range(1, int(number1) + 1):
    for count2 in range(1, int(number2) + 1):

        result = count2 * count1
        if result < 10:
            print(str(count2) + '×' + str(count1) + '=' + str(result).rjust(2), end='')
        else:
            print(str(count2) + '×' + str(count1) + '=' + str(result), end='')

        print()
