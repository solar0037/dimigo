# 20200520_1315.py 사호준

# 리스트내포: 리스트 내에 반복문+조건문
# a 리스트에 3을 곱한 새로운 리스트를 만드세요
a = [1, 2, 3, 4]
result = []
for num in a:  # 반복문
    result.append(num*3)  # append
print(result)

# 리스트내포 이용
a = [1, 2, 3, 4]
result = [num*3 for num in a]  # 리스트 내포
print(result)

# 리스트내포 이용2
a = [1, 2, 3, 4]
result = [num*3 for num in a if num % 2 == 0]  # 리스트 내포
print(result)

# 리스트 내포
# [for 항목 in 반복가능 객체 if 조건]

result2 = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result2)

# 홀수마방진 실습
# Start
# 리스트(배열)의 선언
# 입력값을 받아서 홀수마방진을 출력하는 코드로 변환해주세요.
num = int(input("Enter Num: "))
# 짝수이면 다시 입력받을 수 있도록 한다.
# 홀수이면 아래 코드를 실행(단, 1은 제외한다.)
while num % 2 == 0:
    num = int(input("Enter Num: "))

"""A1315 = [[0 for col in range(6)] for row in range(6)]
i = 1
j = 3

for k in range(1, 26):
    A1315[i][j] = k
    if k % 5 == 0:
        i += 1
    else:
        i -= 1
        j += 1
        if i < 1:
            i = 5
        if j > 5:
            j = 1

for a in range(1, 6):
    for b in range(1, 6):
        print("%2d" % A1315[a][b], end=" ")
    print(' ')"""

A1315 = [[0 for col in range(num+1)] for row in range(num+1)]
i = 1
j = int((num + 1) / 2)

for k in range(1, num ** 2 + 1):
    A1315[i][j] = k
    if k % num == 0:
        i += 1
    else:
        i -= 1
        j += 1
        if i < 1:
            i = num
        if j > num:
            j = 1

for a in range(1, num+1):
    for b in range(1, num+1):
        print("%2d" % A1315[a][b], end=" ")
    print(' ')
