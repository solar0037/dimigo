# 20200632_1315.py 사호준


def add123(a, b):
    return a + b, a * b


result = add123(1, 3)
print(type(result))
print(result)  # *****tuple
# 함수의 반환값은 무조건 한 개

v1 = 1  # 전역변수


def vartest(v1, v2):  # 매개변수
    v1 += 1  # line 17 vs line 13 v1 지역변수
    v2 += 1
    print(v1, v2)  # 지역변수 출력


vartest(1, 3)  # v1=>2 v2=>4
print(v1)  # 1
# print(v2)  # ERROR

# 함수 내에서 선언된 변수는 함수 내부에서만 유효
# 지역변수 vs 전역변수

print("{0:#^100}".format("VARTEST"))
v3 = 1


def vartest2(v3):
    v3 += 1
    return v3


v3 = vartest2(v3)
print(v3)

v4 = 1


def vartest3():
    global v4
    v4 += 1


vartest3()
print(v4)
