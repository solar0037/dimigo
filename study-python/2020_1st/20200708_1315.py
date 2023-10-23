a = []
print(bool(a))
b = {'a': 1, 'b': 2}
print(bool(b))
c1 = ""
c2 = 'Python'

if bool(a) or bool(b):
    print("True")

if 'p' in c2:
    pass
elif 'P' in c2:
    print("True c2 elif")
else:
    print("Else")

# 삼항연산자
score = 90
msg = "'PASS' if score >= 80 else 'FAIL'"  # score>=80 ? 'PASS' : 'FAIL'
print(msg)

a1 = [1, 2, 3, 4]
while a1:
    print(a1.pop())
print(bool(a1))

a2 = (1, 2, 3, 4)
for i in a2:
    print(i*2)
print(a2)
