# 20200826_1315.py 사호준

# 클래스 변수
class a1315:
    c_name = ""


a = a1315()
a.c_name = "사"
b = a1315()
b.c_name = "준"
a = a1315()  # 클래스변수는 동일한 변수를 가리키고 있다.
b = a1315()

print(id(a.c_name))
print(id(b.c_name))

# 모듈
# 사용방법 first
import mod1315  # 파일(스크립트) mod1315
# import mod1315.py (X) !!!!!!
print(mod1315.add(13, 15))
print(mod1315.sub(13, 15))

# 사용방법 second
from mod1315 import *  # mod1315 파일 내의 함수를 가져와
print(add(13, 15))
print(sub(13, 15))

print(mod1315.PI)
c1315 = mod1315.Math()  # 모듈에 정의된 클래스도 사용
print(c1315.solve(2))  # 원의 넓이를 구함.

# 내장함수
# print() len() type() str() int() list() tuple()

# all(반복가능한요소(리스트, 튜플)): 구성요소 중에 False 값이 없을 때 vs any()
print(all([1, 2, 3, 4, 5]))  # True
print(all([0, 1, 2, 3, 4, 5]))  # False
print(all(['a', 'b', '', 'c']))  # False

print(any([1, 2, 3, 4, 5]))  # True
print(any([0, 0, 0]))  # False

# chr(숫자) vs ord(문자): 아스키코드
print(chr(99))
print(ord('A'))

# enumerate: 인덱스값 출력
for i, name in enumerate(['eb', 'dc', 'wp', 'hd']):
    print(i, name)

# eval: eval(expression) 수식
print(eval('1+2'))
print(eval('"aaa"+"bbb"'))
print(eval('chr(97)'))

# map: map(f, data): 함수를 실행
def t_times(x):
    return x*2


print(list(map(t_times, [1, 2, 3, 4])))  # map(함수이름, 자료형)

print(list(map(lambda b: b*2, [1, 2, 3, 4])))
