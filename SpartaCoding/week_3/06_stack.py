class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# stack --> data push, pop이 잦은 자료구조
# LinkedList로 구현
# Stack이라는 클래스를 만들때, 링크드리스트로 만들기 때문에
# 생성시 리스트를 연결하고자 생성자에 구현
class Stack:
    # def __init__(self):
    #   self.head = None
    def __init__(self, value):
        self.head = Node(value)

    def push(self, value):
        # 새로 만든 노드
        # 새로 만든 노드가 가리키는건 가장 머리
        # 가장 머리는 새로운 노드
        # [3] -> [4] (3이 새로 들어오는 것)
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # [3] -> [4]
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        delete_node = self.head
        self.head = self.head.next
        return delete_node

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.head.data

    def isEmpty(self):
        return self.head is None


stack = Stack(1)
stack.push(3)
stack.push(4)
print(stack.peek())
stack.pop()
print(stack.pop().data)
