# w1315_20201123.py


class FixedQueue:
    # 파생클래스 예외처리기법
    class Full(Exception):
        pass

    class Empty(Exception):
        pass
    
    # annotation: 주석, 매개변수, 함수반환값
    # 매개변수: expressino 반환값 -> 자료형
    def __init__(self, capacity: int) -> None:
        self.no = 0  # 원소의 개수
        self.front = 0  # 전위 포인터
        self.rear = 0  # 후위 포인터
        self.capacity = capacity  # 큐의 크기
        self.que = [None] * capacity  # 큐 본체
    
    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity
    
    def __len__(self) -> int:
        return self.no
    
    # enque, deque
    def enque(self, value):
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = value
        self.rear = self.rear + 1
        self.no = self.no + 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> int:
        if self.is_empty():
            raise FixedQueue.Empty
        x =self.que[self.front]
        self.front = self.front + 1
        self.no = self.no - 1
        if self.front == self.capacity:
            self.front = 0
        return x


# ***** 큐의 동작 *****
from enum import Enum
Menu = Enum('Menu', ['Enque', 'Deque', 'Exit'])


def select_menu():
    # se = ['({m.value}){m.name}'.format(m) for m in Menu]
    se = [f'({m.value}){m.name}' for m in Menu]
    # se = ['({0}){1}'.format(m.value, m.name) for m in Menu]
    while True:
        print(*se, sep='   ', end='')
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)


# 큐의 시작
q1315 = FixedQueue(13)  # 큐 클래스 선언
while True:
    print('Que1315 Start : {0} / {1}'.format(
        len(q1315), q1315.capacity)
    )

    menu = select_menu()
    if menu == Menu.Enque:
        x = int(input("Enter data: "))
        try:
            q1315.enque(x)
        except FixedQueue.Full:
            print("Queue Full!!!")
    
    elif menu == Menu.Deque:
        try:
            y = q1315.deque()
            print("Data deque {0}".format(y))
        except FixedQueue.Empty:
            print("Queue Empty!!!")

    else:
        break
