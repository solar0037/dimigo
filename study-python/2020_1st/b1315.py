# b1315.py

# HW 난수(random)을 이용하여 난수(1~100 사이의 수)를 생성한 후
# 어떤 숫자인지 맞추는 프로그램을 만드세요.
# 입력한 숫자가 난수보다 크면 UP, 작으면 DOWN으로 알려주고 계속 추측하여 난수값을
# 만드는 프로그램을 작성하시면 됩니다.

import random

n = random.randint(1, 100)
while 1:
    user_n = input("Guess my number (Q to exit):")
    if user_n in ['Q', 'q']:  # Q(q): quit
        break
    else:
        user_n = int(user_n)
        if user_n < n:  # user_n is lower -> higher!
            print("Choose higher number")
        elif user_n > n:  # user_n is higher -> lower!
            print("Choose lower number")
        else:  # user_n == n
            print("Correct!")
            break
