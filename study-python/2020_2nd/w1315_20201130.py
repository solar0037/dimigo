# w1315_20201130.py

# 11월의 마지막 날...
# collections.deque 스택+큐를 동시에 구현

# append() extend() appendleft() extendleft()
# append(): 원소 입력 vs extend(): 객체의 입력

# pop() popleft() remove() reverse() rotate()
from collections import deque

w1315 = deque([1, 3, 3, 0])
w1315_s = deque(['1', '3', '3', '0'])

w1315.append(13)
w1315.appendleft(14)
print(w1315)

w1315.extend([15])
w1315.extendleft([15])
print(w1315)
print(w1315[6] + w1315[7])  # int + str

w1315_s.append('wp')
w1315_s.extend('wp')
print(w1315_s)
# deque은 원소 수정이 가능함. vs 문자열, 튜플
w1315_s[6] = 'wpwp'
print(w1315_s)
t_str = 'wpwp1315'
# t_str[1] = 'h'  # Error

w1315_s.pop()
print(w1315_s.popleft())  # !!! 반환값이 존재
w1315_s.remove('3')
print(w1315_s.remove('w'))  # 반환값이 없음. => none
print(w1315_s)

print(w1315)
w1315.reverse()  # 역순정렬
print(w1315)
w1315.rotate(2)  # 지정된 숫자만틈 순환
print(w1315)

# Stack with Collections.deque

class Stack1315:
    def __init__(self, maxlen=13) -> None:
        self.capacity = maxlen
        self.stk1315 = deque([], maxlen)  # deque의 초기선언.
        # deque([1, 2, 3]) vs None*capacity
    
    def __len__(self) -> int:  # 연산자 오버로딩
        return len(self.stk1315)
    
    def is_empty(self) -> bool:
        return not self.stk1315

    def is_full(self) -> bool:
        return len(self.stk1315) == self.stk1315.maxlen
    
    # push.pop
    def push(self, value) -> None:
        if self.is_full():
            print("Stack is Full!!!")
        else:
            self.stk1315.append(value)
    
    def pop(self) -> any:
        return self.stk1315.pop()
    
    def dump(self):
        print(list(self.stk1315))
    
    # Peek, find, count
    def peek(self):
        return self.stk1315[-1]  # 파이썬 리스트의 특징
    
    def find(self, value):
        try:
            return self.stk1315.index(value)
        except ValueError:
            return -1
    
    def count(self, value):
        return self.stk1315.count(value)
    
    def __contains__(self, value):
        return self.count(value)


# 스택의 구현
from enum import Enum
Menu = Enum('Menu', ['PUSH', 'POP', 'DUMP', 'PEEK', 'FIND', 'COUNT', 'EXIT'])

def select_menu():
    sel = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*sel, sep='   ', end=' ')
        n = int(input(": "))
        if 1<=n<=len(Menu):
            return Menu(n)


w1315_stk = Stack1315(13)
while True:
    print("Stack with Deque {0}/{1}".format(
        len(w1315_stk), w1315_stk.capacity))
    menu = select_menu()

    if menu == Menu.PUSH:
        try:
            x = int(input("Enter Data:"))
            w1315_stk.push(x)
        except IndexError:  # !!! maxlen: 13 / 14번째 참조
            print("Stack Full!!!")

    elif menu == Menu.POP:
        try:
            y = w1315_stk.pop()
            print(f"Pop data is {y}")
        except IndexError:
            print("Stack empty")

    elif menu == Menu.DUMP:
        w1315_stk.dump()

    elif menu == Menu.PEEK:
        try:
            z = w1315_stk.peek()
            print("Peek Data", z)
        except IndexError:
            print("Stack Empty!!!")

    elif menu == Menu.FIND:
        tmp = int(input("Find Data:"))
        if tmp in w1315_stk:
            print(f"{w1315_stk.find(tmp)}번째 위치에 있고 {w1315_stk.count(tmp)}개 있음.")
        else:
            print("No Find!!!")

    else:
        break
