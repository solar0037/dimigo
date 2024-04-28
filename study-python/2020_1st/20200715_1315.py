# def vs lambda


def addt(x, y):
    return x+y


addt1 = lambda x, y: x+y

print(addt(1, 3))
print(addt1(1, 3))

a = [1, 2, 3]
d2 = {'a': 1, 'b': 2}

if a.sort() == d2.get('c'):
    z = abs(-1)
    print(z)
    print(z, z)
    print("W", "P")
    print("W" "P")
    print('w'+'p')

f = open("test.txt", 'w')
print(type(f))
for x in range(1, 5):
    f.write(str(x))

f.close()
