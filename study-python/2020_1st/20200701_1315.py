t_str = 'PYTHON is very difficult!'

print(type(t_str))

# 인덱싱
print(t_str[3])

# t_str[3] = 'T'

# 슬라이싱
print(t_str[:])
print(t_str[2:5])
print(t_str[:10])
print(t_str[5:-4])  #

print(t_str[1:10:2])  #
print(t_str[::-1])  #
print(t_str[0:10:2])
print("ERR")
print(t_str[1:10:-1])

# 포맷팅
print("I eat %d apples" % 13)
a = 13
print("I eat %d apples" % a)
b = 36
# print("I eat %d apples" % a+b)
print("I eat %d apples" % (a+b))

print("{0:#^100}", format("1301"))
print("{0:@<100}".format("1315"))
print("{0:@>100}".format("1315"))
