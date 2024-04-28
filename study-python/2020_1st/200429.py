# 200429_1315_사호준
# 리스트 내장함수
list = [1, 3, 2, 6, 7, 9, 0]
print(list)

# append(value) 리스트의 맨 마지막에 요소를 추가
list.append(11)
list.append(12)
print(list)

# sort() 오름차순으로 정렬
list.sort()  # 정렬
print(list.sort())  # (X) none = false 반환값은 없어요
print(list)

# reverse() #뒤집기
list.reverse()
# print(list.reverse()) #(X) none = false 반환값은 없어요
print(list)

# index(value) 위치 값 찾기
print(list.index(11))
# print(list.index(29)) #ERROR 찾는 값이 없어서...

# insert(index, value) index위치에 value 값을 넣으세요.
print(list)
list.insert(3, 29)
print(list)

# remove(value) #처음 나오는 valu를 삭제
list.insert(0, 2)
list.insert(0, 2)  # 리스트는 중복값을 허용
list.remove(2)
print(list)
list.remove(2)
print(list)

# pop(index) *****index위치의 값을 반환하고 삭제 / 맨뒤의 값을 반환하고 삭제
print("POP()내장함수")
list.pop()  # 화면에 결과x
print(list.pop())  # 1
print(list)
list.pop(2)
print(list)

# count()
print(list.count(29))
print(list.count(7))  # 문자

# extend() 리스트 붙이기
list.extend([1, 2])  # list+[1, 2]와 같은 결과
print(list)

# reverse()
list1 = [1, 9, 2, 4]
list1.reverse()
print(list1)
list1.insert(1, 3)  # => [3, 4, 2, 9, 1]
# 58번째 수행결과는 [3, 4, 2, 9, 1]이 화면에 출력된다. ( X )
# print(list1)
# 60번째 수행결과는 [3, 4, 2, 9, 1]이 화면에 출력된다. ( X )

# 과제: a$b$c$d$e와 같이 출력하는 코드를 완성해주세요
h1 = "a:b:c:d:e"
h2 = h1.replace(':', '$')
print(h2)

# 과제2: [1333, 1328, 1325, 1317, 1301]와 같이 출력되도록 코드를 완성해주세요.
h3 = [1328, 1301, 1325, 1333, 1317]
# h3.sort()
# h3.reverse()
h3.sort(reverse=True)  # 오름차순 : reverse=false 기본 / 내림차순 : reverse=True
print(h3)

# 튜플 자료형 - 리스트와 동일하나 단 2가지가 달라요
# 수정이 불가능 / 3개의 요소가 있을때는 ,가 반드시
# 배열 = 리스트 = 튜플

t1 = ()  # 빈 튜플
t2 = (1,)  # 요소가 1개 일때 반드시 ","
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# 튜플의 인덱싱, 슬라이싱, +, *
print(t3[1])
print(t3[1:])
print(t3 + t4)
print(t3 * 2)

# 튜플은 () 또는 ()없이 표현되나 수정불가능
# t3[1] = 4
# del t3[1]
print(t3)

# len()
print(len(t3))

# 딕셔너리 : 페어 key:value
# 연관배열(Associative array) : 페어, 해쉬(HASH) : 문자열을 간소화 치환, 암호화(X)

# 변수명={key1:value1, key2:value2, key3:value3}
dic = {'name': '사호준', 'class': 'wp', 'num': 15}
print(dic)
dic1 = {1: 'a', 2: 'b'}  # key가 숫자로 지정할 수 있음.
dic1[3] = 'c'  # 자료추가 변수명[key]=value
print(dic1)

# 라스트=[] 튜플=() 딕셔너리={}

del dic1[2]  # 자료삭제 변수명[key]
print(dic1)

# 딕셔너리 자료형의 활용
print(dic['name'])

# 유의할점
dic2 = {1: 'a', 2: 'b', 3: 'c', 1: 'd', 2: 'e'}  # 딕셔너리 자료형은 key의 중복을 허용하지 않습니다.
print(dic2)

# dic3 = {[1, 2]: 'a', [3, 4]: 'b'}  # key는 리스트형이 올 수 없습니다.

# dic 함수******
# get()
print(dic.get('birth'))  # key가 없는 값을 출력하고자 할때 None=False 거짓
# print(dic['birth'])  # key가 없는 값을 출력하고자 할때 Error

# keys()
print(dic.keys())  # 딕셔너리의 키를 모아서 출력

# items()
print(dic.items())  # 딕셔너리의 키와 값을 쌍으로 출력

# values()
print(dic.values())  # 딕셔너리의 값만 모아서 출력

# in key가 딕셔너리에 있는지 확인
print('name' in dic)


t2 = (1,)
t3 = ('a')
print(type(t2), type(t3))
