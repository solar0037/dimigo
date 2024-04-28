# w1315_20201228.py

# 리스트 / 단일(연결) 리스트

# python list with class


class Node:
    # 연결리스트 노드 클래스
    def __init__(self, data, next) -> None:  # 매개변수 data, next <= 클래스 선언시 매개변수
        self.data = data  # 데이터
        self.next = next  # 뒤쪽 포인터


class LinkedList:
    # 연결 리스트 클래스
    def __init__(self) -> None:
        self.no = 0  # 노드의 개수
        self.head: Node = None  # Head Node
        self.current: Node = None  # Current Node
    
    def __len__(self) -> int:
        return self.no
    
    def add_first(self, data) -> None:
        # Head 부분에 노드를 삽입
        ptr = self.head  # 넣기 전에 Head 부분
        self.head = self.current = Node(data, ptr)
        self.no += 1
    
    def add_last(self, data) -> None:
        # 맨 마지막에 노드를 추가
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head  # ptr:  임시 포인터
            while ptr.next is not None:
                ptr = ptr.next

            ptr.next = self.current = Node(data, None)
            self.no += 1
    
    def remove_first(self) -> None:
        # 맨 처음 노드 삭제
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self) -> None:
        # 맨 마지막 노드 삭제
        if self.head is not None:  # 빈 연결리스트가 아닐때
            if self.head.next is None:  # 노드가 1개 뿐일때
                self.remove_first()
            else:
                ptr = self.head  # 스캔 중 노드
                pre = self.head  # 스캔 중 노드의 앞쪽 노드
                while ptr.next is not None:  # 꼬리노드 찾기
                    pre = ptr  # pre 꼬리노드의 바로 앞쪽
                    ptr = ptr.next
                pre.next = None  # pre 삭제뒤에 꼬리노드
                self.current = pre
                self.no -= 1

    def remove(self, p) -> None:
        # 중간 노드 p
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next = p.next
                self.current = ptr
                self.no -= 1
    
    #************************
    def print(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def search(self, data):
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

# 연결리스트 구현
from enum import Enum
Menu = Enum('Menu', ['InsertHead', 'InsertTail', 'DeleteHead', 'DeleteTail', 'NodePrint', 'Search', 'Exit'])


def select_Menu():
    sel = [f'({m.value}){m.name}' for m in Menu]
    print(*sel, sep='   ', end='')
    n = int(input(": "))
    if 1 <= n <= len(Menu):
        return Menu(n)


lst1315 = LinkedList()  # 객체선언
while True:
    menu = select_Menu()

    if menu == Menu.InsertHead:
        lst1315.add_first(int(input("Enter Data=>")))
    elif menu == Menu.InsertTail:
        lst1315.add_last(int(input("Enter Data=>")))
    elif menu == Menu.DeleteHead:
        lst1315.remove_first()
    elif menu == Menu.DeleteTail:
        lst1315.remove_last()
    elif menu == Menu.NodePrint:
        lst1315.print()
    elif menu == Menu.Search:
        pos = lst1315.search(int(input("Find Data=>")))
        if pos>=0:
            print("Data Position {0}".format(pos+1))
        else:
            print("Not Found!")
    else:
        break
