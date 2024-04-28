# 20200508_1315.py 사호준

# 제어문
money = True  # 변수 money는 불형 자료형
if money:  # if 조건문:
    print('치킨을 먹다.')  # 스페이스 4칸 또는 Tab키
else:
    print('잠을 잔다.')

# 제어문 확장
money = 15000
card = True
if money >= 20000 or card:  # and or not
    print('치킨을 먹다.')
else:
    print('잠을 잔다.')

# 비교연산자 < > <= >= == !=
# =(대입연산자) vs ==(비교연산자)
# in 연산 vs not in 연산
money = 0
if money == 0:
    print('치킨을 먹다.')
else:
    print('잠을 잔다.')

a = [1, 2, 3]
print(1 in a)
b = 'python'
print('j' not in b)

pocket = ['paper', 'phone', 'money', 'card']
if 'money' in pocket:
    pass
else:
    print('잠을 잔다')

# 한줄쓰기
pocket = ['paper', 'phone', 'money', 'card']
if 'money' in pocket:
    pass
else:
    print('잠을 잔다')

a = 'Korea Digital Media High School WP 1401'

if 'high' in a: print("high")
elif 'Digital' in a and 'Analog' in a: print("Digital")
elif 'korea' not in a: print('korea')
elif 'WP' in a: print("WP")
else: print("None")

pocket = ['paper', 'phone']
card = True
if 'money' in pocket:
    print('치킨을 먹다')
elif card:
    print('치킨을 카드로 먹다.')
else:
    print('잠을 잔다.')

# 조건부 표현식
score = 90
if score >= 80:
    print('합격')
else:
    print('불합격')

# 구조: 조건문이 참일 경우 if 조건문 else 거짓일 때
print('합격') if score >= 80 else print('불합격')
k = '합격' if score >= 80 else '불합격'  # 3항 연산자
