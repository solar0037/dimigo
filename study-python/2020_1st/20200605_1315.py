# 20200605_1315.py 사호준

# lambda 사용자 정의함수

# def add(a+b):
#   return a+b
add = lambda a, b: a+b  # 1. () 괄호 없음, return 예약어 없음
result = add(1, 3)
print(result)

print('1''2''3')
print('1', '2', '3')

# 파일
f = open('test1315.txt', 'w')  # f 파일포인터
for i in range(1, 11):
    data = "%d번째 줄\n" % i
    f.write(data)  # 파일쓰기
f.close()  # 파일닫기

# readline
f = open('test1315.txt', 'r')  # 읽기모드 r
while True:
    line = f.readline()  # 한줄씩 읽어옴
    if not line:
        break
    print(line)
f.close()

# readlines()
f = open('test1315.txt', 'r')  # 읽기모드 r
lines = f.readlines()  # 리스트로 반환
for line in lines:
    print(line)
f.close()
print(type(lines))
print(type(line))

# read()
f = open('test1315.txt', 'r')
data = f.read()  # 한꺼번에 문자열로 앍어옴.
print(data)
f.close()

# write 모드와 추가모드
f = open('test1315.txt', 'a')  # f 파일포인터
for i in range(11, 21):
    data = "%d번째 줄\n" % i
    f.write(data)  # 파일쓰기
f.close()  # 파일닫기

# with
with open('test1315.txt', 'a') as f:
    f.write('Python')
# f.close() 사용하지 않아도 자동으로 닫혀요
