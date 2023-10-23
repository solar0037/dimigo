#200422.py
#1315 사호준

#포매팅
a="I ate %d apples." %1315
print(a)
print(type(a)) #type() 자료형을 확인하는 내장함수 =>str
num=1315
print(type(num))
print("I ate %d apples." %num)
print("I ate %s apples." %'사호준')
print("I ate %s apples." %1315) #숫자가 문자열로 자동형변환
#print("I ate %d apples." %'1301') #문자를 숫자로 표현할 수 없음.

print("I ate %d apples. so I was sick %s days" %(1315, 'five'))
days='five'
print("I ate %d apples. so I was sick %s days" %(1315, days))

print("Error %d%%" %100)

#정렬
print('%20s'%'hi')
print('%-20s'%'hi')

b="KOREA DIGITAL MEDIA HIGH SCHOOL"
print(b[:]) #모두 출력
print(b[::2]) #간격
print(b[1::2]) #시작
print(b[::-1])

print("%0.4f"%3.141592)
print("%-20.4f"%3.141592) # %10.4f -> %20.4f -> -20.4f

#format함수를 이용한 포매팅
print("I ate {0} apples.".format(1315)) #.
print("I ate {0} apples. so I was sick for {1} days".format(1315, "six"))
print("I ate {0} apples. so I was sick for {days} days".format(1315, days=5))
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi")) #가운데 정렬

print("{0:=<10}".format("hi"))
print("{0:*<10}".format("hi"))
print("{0:!^10}".format("hi"))#가운데 정렬

#F문자열 3.6이상 지원 *변수의 참조가 가능
name="사호준"
age=17
# 밑줄(__) 또는 영문자로 시작 / 숫자와 영문자 혼용 / 특수문자 불가
#변수명 폴더명 / 대소문자는 구분 Name != name

print(f'my name is {name}, age is {age+1}.')
print(f'{"hi":%<10}')
print(f'{"hi":&>10}')
print(f'{"hi":#^10}')

#문제: format 함수 또는 f문자열 포맷팅을 사용해서 '#####Sa Hojun#####'를 출력하는 코드를
#아래에 작성해주세요
print("{0:#^18}".format("Sa Hojun"))
print(f'{"Sa Hojun":#^18}')

#묹자열 관련함수
#len() type() print()
print(b)
print(b.count('D')) #b문자열에서 'd'의 갯수
#find() index()
print(b.find("d")) # 찾는 문자가 없을때 반환값 -1
print(b.index("D")) # ERROR 찾는 문자가 없을 때 ERROR

print("#".join("abcde"))

#upper() 대문자로, lower() 소문자로
print(b.lower())

print(b.replace("MEDIA", "ANALOG"))

#split()
print(b.split()) #리스트로 분할출력
print(b.split(" "))
print(b.split("H"))
