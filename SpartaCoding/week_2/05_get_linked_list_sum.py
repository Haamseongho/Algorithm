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


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!
    sum1 = get_linked_list_sum_data(linked_list_1)
    sum2 = get_linked_list_sum_data(linked_list_2)
    ans = sum1 + sum2
    return ans


def get_linked_list_sum_data(linked_list):
    linked_list_sum = linked_list.head.data
    while linked_list.head.next is not None:
        linked_list_sum = linked_list_sum * 10 + linked_list.head.next.data
        linked_list.head = linked_list.head.next

    return linked_list_sum


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
