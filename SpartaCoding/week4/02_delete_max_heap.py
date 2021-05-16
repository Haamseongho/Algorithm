class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        root_node = self.items.pop()  # 위에서 변경한 다음에 pop하기
        parent_index = 1
        while parent_index <= len(self.items):
            left_child_index = parent_index * 2
            right_child_index = parent_index * 2 + 1
            # 자식이 더 없는 경우(leaf node)
            max_index = parent_index
            if left_child_index >= len(self.items) or right_child_index >= len(self.items):
                break

            # 힙정렬이 멈추지 않고 지속해서 체크하는 방향으로 진행
            if self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index
            if self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index
            if max_index == parent_index:  # 자식노드와의 변동이 없다면 힙정렬이 완료된 상태
                break

            self.items[parent_index], self.items[max_index] = self.items[max_index], self.items[parent_index]
            parent_index = max_index

        return root_node  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]
