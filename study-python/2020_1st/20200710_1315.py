for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)
    print("")

for i in "Python":
    print(i, type(i))

# sum = 0
for j in [1, 2, '3', 4, 5]:
    print(j, type(j))
    # sum += j

def add_many(*args):
    result = 0
    for i in args:
        result += i
    print(type(args))
    return result, result + 1

k = add_many(1, 2, 3, 4 ,5)
k1, k2 = add_many(1, 2, 3)
print(k, type(k))
print(k1, k2, type(k1), type(k2))

def kk1(**k_arg):
    return k_arg

tmp1 = kk1(a=1, b=2)  # !!!!!
print(tmp1, type(tmp1))

d1 = {'a': 1, 'b': 2}
print(d1)

v1 = 1
def vtest(a):
    global v1
    v1 = v1 + 1

vtest(1)
print(v1)
