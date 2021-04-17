class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # 다음 노드를 가리키는 것 정리



# LinkedList는 self.head에 시작하는 노드를 저장한다.
# 다음 노드를 보기 위해서는 next로 접근

class LinkedList: # head node만 가지고 있으면 됨
    # Node 정보를 만들어서 넣기
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head # 현재 head 노드 위치
        # head node를 따라 계속 next로 따라가기
        # cur.next -> 다음 노드 이걸 cur로 두면서 head 바꾸기기        while cur.next is not None:
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
    def print_all(self):
        print("hello")
        cur = self.head
        while cur is not None: # head가 아무것도 없지 않다면 head의 데이터 출력
            # head는 다음꺼로 계속 갱신
            print(cur.data)
            cur = cur.next

node1 = LinkedList(3)
node1.append(5)
node1.append(7)

node1.print_all()