# 20200617_1315.py 사호준

# 1. 1000보다 작은 자연수 중에서 3 또는 5의 배수를
# 모두 더하는 프로그램을 작성하시오.

sum_t = 0  # 변수 저장할 공간
# 논리적 연산
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:  # i%3==0 || i%5==0
        sum_t += i  # sum_t = sum_t + i

print(sum_t)  # 출력

# 피보나치 수열
# 2. 피보나치 수열에서 400만 이하면서 짝수인 항의 합을 구하는
# 프로그램을 작성하시오.
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...


sum_t2 = 0
a = 1
b = 1
# 피보나치논리
while a <= 4000000:
    if a % 2 == 0:
        sum_t2 += a
    a, b = b, a + b  # !!!
print(sum_t2)

'''
import webbrowser as wb
url = "http://jhserver.dimigo.hs.kr/test.html"
wb.open_new(url)
'''

# 3. 문자열을 입력 받아 같은 문자가 연속적으로 반복되는 경우에
# 그 반복 횟수를 표시해 문자열을 압축하여 표시하는 프로그램을 작성하시오.
# 입력예시 : aaabbcccccca
# 출력예시 : a3b2c6a1

# str_tmp = input("Enter Str: ")  # python
# result = ""
# for i in str_tmp:  # python => str_tmp[0] => str_tmp[5]
#     print(i)  # !!!
#
# print(result)

str_tmp = input("Enter Str: ")
tmp_t = ""
cnt = 0
result = ""
for c in str_tmp:
    if tmp_t != c:
        tmp_t = c
        if cnt:
            result += str(cnt)
        result += c
        cnt = 1
    else:
        cnt += 1
if cnt:
    result += str(cnt)

print(result)

# 모스부호
dic = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
       '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
       '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'
       }


def morse(t_str):
    result = []
    for word in t_str.split(" "):  # split(기준문자)
        for char in word.split(" "):
            result.append(dic[char])  # dic[char] => key
        result.append(" ")
    return "".join(result)  # join


print(morse('.--. -.-- - .... --- -.'))
