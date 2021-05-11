top_heights = [6, 9, 5, 7, 4]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        delete_node = self.head
        self.head = self.head.next
        return delete_node

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.head

    def is_empty(self):
        return self.head is None


def get_receiver_top_orders(heights):
    n = len(heights)
    tower_inx_stack = [0] * n  # 0으로 초기화 하는 방법

    while heights:  # heights가 존재할 때 반복문 돌기
        tower = heights.pop()
        n = len(heights)  # 길이를 설정하고 스택에서 pop하기 떄문에 길이는 지속해서 하나씩 줄어듬
        for idx in range((n - 1), 0, -1):  # range에 특성: 시작점, 종료점, 증감값
            if tower < heights[idx]:  # 스택 길이만큼 (pop했으니까 그만큼 줄어든 길이) 반복을 돌려서 비교구문 수행
                tower_inx_stack[n] = idx + 1  # 인덱스로 돌리기 때문에 위치는 +1 해서 값을 넣을 것
                break

    return tower_inx_stack


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
