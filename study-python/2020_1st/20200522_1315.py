# 20200522_1315.py 사호준

"""# 배열 달팽이
# Start
# 배열의 선언
A1315 = [[0 for col in range(6)] for row in range(6)]  # 6*6배열

k = 0
sw = 1
i = 1
j = 0
n = 5

while True:
    for p in range(1, n + 1):
        k = k + 1
        j = j + sw
        A1315[i][j] = k
    n = n - 1
    if n > 0:
        for p in range(1, n + 1):
            k = k + 1
            i = i + sw
            A1315[i][j] = k
        sw = sw*(-1)
    else:
        break

for a in range(1, 6):
    for b in range(1, 6):
        print("%3d" % A1315[a][b], end=" ")
    print(' ')"""

# 배열 달팽이
# Start
# 단 1이 입력되면 종료
# 배열의 선언
while True:
    num = int(input("Enter Num: "))
    if num == 1:
        break

    A1315 = [[0 for col in range(num + 1)] for row in range(num + 1)]  # 6*6배열

    k = 0
    sw = 1
    i = 1
    j = 0
    n = num

    while True:
        for p in range(1, n + 1):
            k = k + 1
            j = j + sw
            A1315[i][j] = k
        n = n - 1
        if n > 0:
            for p in range(1, n + 1):
                k = k + 1
                i = i + sw
                A1315[i][j] = k
            sw = sw * (-1)
        else:
            break

    for a in range(1, num + 1):
        for b in range(1, num + 1):
            print("%3d" % A1315[a][b], end=" ")
        print(' ')
