class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



node = Node(3)
print(node.data)

first_node = Node(4)

node.next = first_node # [3] -> [4]
print(first_node.data)
print(node.next.data) # [3] -> [4].data


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

        print(cur.data)
node1 = LinkedList(3)
print(node1.head)
print(node1.head.data)
print(node1.head.next)