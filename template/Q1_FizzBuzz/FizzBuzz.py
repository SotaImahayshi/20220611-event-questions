for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 15 == 0:            #15の倍数の場合（数字の代わりにFizzBuzzと出力する）
        string = "FizzBuzz"
    elif num % 5 == 0:           #5の倍数の場合（数字の代わりにBuzzと出力する）
        string = "Buzz"
    elif num % 3 == 0:           #3の倍数の場合（数字の代わりにFizzと出力する）
        string = "Fizz"
    else:                        #3,5,15の倍数以外の場合（そのまま数字を出力する）
        string = num
    # ここまで記述

    print(string)
