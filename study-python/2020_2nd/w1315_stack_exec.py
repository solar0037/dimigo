# 1315_stack_exec.py
from enum import Enum
from w1315_20201113 import FixedStack1315


Menu = Enum('Menu', ['PUSH', 'POP', 'PEEK', 'EXIT'])
def select_menu():
    s = [f"({m.value}){m.name}" for m in Menu]  # 문자열 포매팅 + 리스트 내포
    while True:
        print(*s, sep='    ', end=' ')
        n = int(input(':'))
        if 1 <= n <= len(Menu):
            return Menu(n)

s1315 = FixedStack1315(13)  # 사용자 입력 저장공간 13=capacity

while True:
    print(f"Now Stack: {len(s1315)}/{s1315.capacity}")
    menu = select_menu()

    if menu == Menu.PUSH:
        x = int(input("Enter Data:"))
        try:
            s1315.push(x)
        except FixedStack1315.Full:
            print("Stack Full!!!")

    elif menu == Menu.POP:
        try:
            y = s1315.pop()
            print(y, 'is POP!')
        except FixedStack1315.Empty:
            print("Stack Empty!!!")

    elif menu == Menu.PEEK:
        try:
            z = s1315.peek()
            print('Peek Data:', z)
        except FixedStack1315.Empty:
            print("Stack Empty!!!")

    else:
        break

