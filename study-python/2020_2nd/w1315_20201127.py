# w1315_20201127.py

# annotation and collections.deque module
# annotation: 주석, 매개변수의 자료형, 함수의 반화값 자료형 주석
# 강제성이 없음

def func(arg1: str, arg2: int, arg3: "1-3WP") -> bool:
    print(arg1, arg2, arg3)
    print(func.__annotations__)  # 함수의 annotation 출력
    return True


func(13, '1-3', True)  # int str bool

# collections.deque: 스택과 큐를 한번에 만들 수 있는 모듈
# append(), extend()

w1315_data = [1, 2, 3, 4, 15]
w1315_data1 = ['a', 'b', 'c', '15']

from collections import deque

deque_w1 = deque(w1315_data)
print(deque_w1, type(deque_w1))
deque_w1.append(5)  # 마지막에 넣어요
deque_w1.appendleft(6)  # 처음에 넣어요
print(deque_w1)
deque_w1.pop()
deque_w1.popleft()
print(deque_w1)

deque_w1.append(5)  # 원소
deque_w1.extend([5])  # 객체 .extend(5) => Error
print(deque_w1)

deque_w2 = deque(w1315_data1)
deque_w2.append('f')
deque_w2.extend('g')
print(deque_w2)

deque_w2.append('hi')
deque_w2.extend('jk')
deque_w2.extend(['lm', 'no'])
print(deque_w2)

# 선형(자료)구조: 스택, 큐, 덱, 리스트
# 원형큐 + 덱
# FIFO: 큐 LIFO: 스택
# 덱: 양쪽으로 입출력이 가능한 => collections.deque
# deque(a): 선언 a=> iterable 변수
# append(원소) / appendleft(원소)
# pop() / popleft()
# extend(반복 가능한 변수) / extendleft(반복 가능한 변수)
# extend("abc") vs extend(["abc"])
