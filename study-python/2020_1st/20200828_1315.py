# 20200828_1315.py 사호준

import mod0828_1315
print("20200828_1315.py exec:", __name__)

print(mod0828_1315.PI)
m1315 = mod0828_1315.Math()  # m1315 객체는 mod0828_1315.Math 클래스의 인스턴스입니다.
print(m1315.solve(3))
# 반지름이 5인 원의 둘레를 구하는 코드를 넣으세요.
print(m1315.circum(3))
# isinstance
# 객체와 인스턴스
print(isinstance(m1315, mod0828_1315.Math))  # True
# round: 반올림
print(round(3.141592, 2))  # 자리수
print(round(3.141592))  # 기본값

# divmod: 몫과 나머지를 반환(튜플)
print(divmod(8, 3))

# sorted: 정렬
print(sorted([1, 5, 4, 2]))
print(sorted('agcf'))

# ***eval(expression) 수식
print(eval('1'+'2'))
aaabbb = "사호준"
print(eval('aaa'+'bbb'))
print(eval('chr(65)'))
