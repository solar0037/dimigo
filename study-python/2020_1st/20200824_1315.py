# 20200824_1315.py
# 클래스싕 상속, 메소드 오버라이딩, 오버로딩


class cal1315:
    def __init__(self, first, second):
        # __init__예약어 => 초기화 => 객체 생성자
        # 객체를 선언할 때 자동으로 실행하는 함수(=method)
        self.first = first  # self => cal1315 => cal1315.first=first(13)
        self.second = second

    def add(self):  # self => cal1315
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

    def __add__(self, other):
        # 연산자 오버로딩:
        # __add__ = '+' => 객체 + 객체
        print("연산자 오버로딩 %d %d" % (self.first, other.first))


class cal1315more(cal1315):
    # !!!class 하위클래스명(상위클래스명)
    def pow(self):
        result = self.first ** self.second
        return result

    def div(self):
        # 함수(메소드) 재정의 = 메소드오버라이딩
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

    def addmul(self):
        # 더하기연산과 곱하기연산을 동시에 수행하여
        # 튜플로 반환
        # (13, 15) => (28, 195)
        result_add = self.first + self.second
        result_mul = self.first * self.second
        return result_add, result_mul


# 객체의 선언
a1315 = cal1315(13, 15)  # __init__ 변수에 값을 저장
print(a1315.add())
print(a1315.sub())

b1315 = cal1315more(13, 15)
print(b1315.add())
print(b1315.pow())
print(b1315.div())
print(b1315.addmul())

a1315 = cal1315(13, 0)
b1315 = cal1315more(13, 0)
# print(a1315.div())
print(b1315.div())
a1315+b1315
