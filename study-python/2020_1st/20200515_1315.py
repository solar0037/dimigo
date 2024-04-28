# 20200515_1315.py

# for문
test_list = [1, 2, 3, 4]
for i in test_list:  # for 변수 in 리스트 또는 튜플
    print(i)

test_a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in test_a:
    print(first + last)

marks = [90, 70, 25, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

number = 0
for mark in marks:
    number = number + 1
    if mark <= 60:
        continue
    print("%d번 학생은 합격입니다." % number)

number = 0
for mark in marks:
    number = number + 1
    if mark <= 60:
        break
    print("%d번 학생은 합격입니다." % number)

# range 객체
b = range(10)
print(type(b))

sum1 = 0
for i in range(1, 11):
    sum1 = sum1 + i
print(sum1)

# 중첩된 for
for i in range(1, 10):  # 1~9
    for j in range(1, 10):  # 1~9
        print("%2d" % (i*j), end=" ")  # !!!, end=" "
    print(' ')

a = [1, 2, 3, 4]
print(sum(a))
