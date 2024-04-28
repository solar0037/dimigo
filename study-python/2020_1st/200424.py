#200424 1315 사호준

a="Korea Digital Media High School"
print(a.upper())
print(a.count('d'))

a = "Korea Digital Media High School"
a=a.upper()
print(a.lower())
print(a.count('d'))

#슬라이싱 확장
print(a[:]) #문자열변수[시작:끝]
print(a[0:])
print(a[1:3])
print(a[:15])

print(a[::]) #전체 문자열변수[시작:끝:STEP]
print(a[0::]) #전체
print(a[::1]) #전체 a[0] a[1] a[2]...
print(a[::2]) #a[0] a[2] a[4] a[6]...
print(a[1::2]) #a[1] a[3] a[5] a[7]...
print(a[::-1]) #a[-1] a[-2] a[-3]...
print(a[0::-1]) #a[0] a[-0]

print(a.split())
#print(a.split("")) #문법적으로 지원불가
print(a.split(" ")) #split() 동일
print(a.split('H')) #기준문자는 출력 X
b=a.split(' ')
print(len(b)) #리스트 원소수
print(len(a)) #문자열의 길이
print(a.count('')) #


h="Korea Digital Media High School"
print(len(h))
print(h.count(""))
print(len(b))
print(type(b))
print(len(h))
print(type(h))

#리스트 자료형
a1=[1, 2, 3, 4]
a2=['a', 'b', 'c', 'd']
a3=[1, 2, 'a', 'b']
a4=[1, 2, [1, 2]]
a5=[1, 2, ['a', 'b', ["life", "Python", "ㅠ.ㅠ"]]]
a6=list() #함수형
a7=[]

print(a6)
print(a7)

#인덱싱과 슬라이싱
print(a5[0])
print(a5[2][2])
print(a5[2][2][2])

print(a5[:])
print(a5[0:2])

#리스트 연산 + *
print(a1+a2)
print(len(a1)) #a1의 원소수
print(a1*3)
print(len(a1*3)) #a1*3의 원소수
