# 20201113_1315.py


class FixedStack1315:
    # 고정길이 스택 클래스
    def is_empty(self) -> bool:
        # 스택이 비어 있는가? 언더플로
        return self.ptr <= 0  # 조건문 => 부울형(True / False)
    
    def is_full(self) -> bool:
        # 스택이 비어 있는가? 언더플로
        return self.ptr >= self.capacity
    

    # 파생클래스 예외처리 기법: 강제로 예외처리를 발생하여 스택프로그램 운용
    class Empty(Exception):
        pass


    class Full(Exception):
        pass


    # 초기화
    def __init__(self, capacity=256) -> None:
        self.stk1315 = [None] * capacity  # 스택 저장용량의 기본값
        self.capacity = capacity  # 사용자 입력 저장용량
        self.ptr = 0  # 스택포인터

    # PUSH, POP, PEEK
    def push(self, value) -> None:
        if self.is_full():
            raise FixedStack1315.Full
        self.stk1315[self.ptr] = value
        self.ptr += 1
    
    def pop(self) -> any:
        if self.is_empty():
            raise FixedStack1315.Empty
        self.ptr -= 1
        return self.stk1315[self.ptr]
    
    def peek(self) -> any:  # 최상위 데이터 확인
        if self.is_empty():
            raise FixedStack1315.Empty
        return self.stk1315[self.ptr-1]
    
    def __len__(self):  # 오버로딩된 len
        return self.ptr  # ptr 스택에 저장된 자료의 수
    
    # 추가기능구현
    # clear: 스택비우기, find: 원소 찾기, dump: 전체출력, count: 원소수
    def clear(self):
        self.ptr = 0
    
    def find(self, value):
        for i in range(self.ptr-1, -1, -1):
            if self.stk1315[i] == value:
                return 1
            return -1
    
    def dump(self):
        if self.is_empty():
            print("Stack Empty!!!")
        else:
            print(self.stk1315[:self.ptr])
    
    def count(self, value):
        c = 0
        for i in range(self.ptr):
            if self.stk1315 == value:
                c += 1
        return 1
    
    def __contains__(self, value):
        return self.count(value)
