class MaxHeap:
    def __init__(self):
        self.items = [None]  # 완전이진트리 표현할때 맨처음에는 none 기입
        # 부모노드 // 2
        # 왼쪽자식 = 부모노드 * 2
        # 오른쪽자식 = 부모노드 * 2 + 1

    def insert(self, value):
        # 구현해보세요!
        # 현재 level 체크
        self.items.append(value)
        index = len(self.items) - 1  # 마지막에 입력된 위치
        # 부모노드: 현재 입력되는 위치에 // 2

        # 부모노드가 0보다 커야하고 (= 최상위 노드가 아님) 부모노드가 자식노드보다 커야함
        # 만약 위 조건을 만족하지 않는다면 힙구조가 아니기 때문에 탈출

        # 1. 먼저 값을 리스트에 넣는다.
        # 2. 넣은 값의 위치를 뽑아온다. (리스트의 전체 길이 - 1 = 현재 인덱스)
        # 3. 현재 인덱스가 최상위 노드가 된다면 더이상 진행하지 않는다. == 최상위 노드의 인덱스는 1이기 때문에 1 이하가 될 경우 조건문 종료
        # 4. 부모 노드는 현재 노드를 2로 나눈 몫
        # 5. 부모 노드 < 자식 노드(현재 비교할 노드) -> 위치 변경
        # 6. 자식 노드(현재 비교할 인덱스) = 부모 노드의 인덱스 (5가 실행될 경우)
        # 7. 5의 경우가 아니라면 break (반복문을 더이상 수행할 필요가 없다.)
        while index > 1:
            parent_index = index // 2
            if self.items[parent_index] < self.items[index]:
                self.items[parent_index], self.items[index] = self.items[index], self.items[parent_index]
                index = parent_index
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
