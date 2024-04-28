A = [[0 for col in range(5)] for row in range(5)]

K, SW, i, j, N = 0, 1, 0, -1, 5

while True:
    for p in range(0, N):
        K += 1
        j += SW
        A[i][j] = K
    N -= 1

    if N > 0:
        for p in range(0, N):
            K += 1
            i += SW
            A[i][j] = K
        SW *= -1
    else:
        break

for i in range(0, 5):
    for j in range(0, 5):
        print("%2d" % A[i][j], end=" ")
    print(" ")
