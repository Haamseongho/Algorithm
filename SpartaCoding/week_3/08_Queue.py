class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # head    tail      tail
    # [4]  ->  [2]   -> [3]
    # [3]
    def enqueue(self, value):
        # 어떻게 하면 될까요?
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return

    # head    tail
    # [4] [2] [3]
    # [2] [3]
    def dequeue(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "queue is empty"
        delete_node = self.head
        self.head = self.head.next
        return delete_node.data

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "queue is empty"
        return self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None


queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
queue.dequeue()
queue.enqueue(5)
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())