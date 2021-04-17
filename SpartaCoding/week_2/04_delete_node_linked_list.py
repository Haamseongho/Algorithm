class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        inx = 0
        while inx < index:
            cur = cur.next
            inx += 1
        return cur  # 걸리지 않으면 그냥 반환

    # 몇 번째 추가
    def add_node(self, index, value):
        new_node = Node(value)  # [6](집어 넣으려고 하는 노드)
        if index == 0:  # 가장 처음에 들어가야 함
            # 처음 해드가 새로운 노드란걸 가리켜야함
            new_node.next = self.head  # 새로 들어온 노드가 대가리를 가리키고 (대가리는 여기서 [5])
            self.head = new_node  # 새로 들어온 노드가 여기의 대가리가 된다.
            return

        node = self.get_node(index - 1)  # 현재 넣으려고 하는 위치 전의 노드를 가지고 옴 [5]
        next_node = node.next  # 기존에 [5]가 가리켰던 다음 노드인 [12]
        node.next = new_node  # 기존 [5]가 이제는 새로운 노드인 [6]을 가리킨다.
        new_node.next = next_node  # 새로운 노드인 [6]은 기존 다음 노드였던 [12]를 가리킨다.

    # index 번째 노드를 삭제
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
        node = self.get_node(index - 1)
        node.next = node.next.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

# 5를 가지고 와야지만 그 다음에다가 넣을 수 있음
# [5] -> [12] -> [8]
# [6]을 5와 12 사이
linked_list.add_node(1, 6)
linked_list.delete_node(3)
linked_list.print_all()
# -> 5를 들고 있는 노드를 반환해야 합니다!
