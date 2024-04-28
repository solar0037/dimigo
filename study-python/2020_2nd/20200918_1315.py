# 20200918_1315.py 사호준

# 연산
import numpy as np  # alias : 재명명

w1315a = np.array([[1, 2, 3], [7, 8, 9]])  # 2-D
w1315b = np.array([4, 5, 6])  # 1-D
w1315c = np.array([[1, 3], [1, 5]])
w1315d = np.array([13, 15])

# 배열의 사칙연산, 차원이 다른 배열의 사칙연산(브로드캐스팅) 가능
print(w1315a+w1315b)
print(w1315a-w1315b)
print(w1315a*w1315b)  # 곱셈
print(w1315a/w1315b)
print(np.dot(w1315c, w1315d))  # !!!행렬의 내적

# arange(시작, 끝) : 시작부터 끝-1 까지 구성된 배열 생성
w1 = np.arange(1, 1315)
print(w1)
w2 = np.arange(1, 13, dtype=float)
print(w2)
w3 = np.random.randn(3, 3)  # 2-D 9개 요소
print(w3)
w4 = np.random.randint(10, size=(3, 3))  # 10까지의 숫자중
print(w4)
w5 = np.random.randn(10)
print(w5)
w6 = np.arange(1, 25)
w7 = w6.reshape(4, 6)
print(w7)
print(w7.sum())
print(w7.sum(axis=0))
print(w7.mean())
print(w7.mean(axis=1))
print(w7.max(), w7.min())

w8 = np.zeros(10, dtype=int)  # 10개의 요소가 모두 0인 1-D 배열 생성
w9 = np.ones((3, 5), dtype=float)  # 요소가 모두 1인 3*5 float 배열 생성
print(w8, w9)

# matplotlib
import matplotlib
import matplotlib.pyplot as plt
w10 = np.random.randn(1000)
w11 = np.random.normal(0, 1, 1000)
print(w10)
plt.grid()  # 그리드 표현
plt.hist(w11)  # 히스토그램으로 표현
# plt.plot(w11)
plt.show()
# randn vs rand vs normal
# randn == normal
# rand 0<r<1 난수
