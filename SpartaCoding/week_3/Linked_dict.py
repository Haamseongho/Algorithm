class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedTuple:
    def __init__(self):
        self.items = list()  # 리스트로 만들어주기

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v

# Chaining 방법
class LinkedDict:
    def __init__(self):
        self.items = [] # [LinkedTuple(),LinkedTuple(),LinkedTuple(), ... ]
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        # LinkedTuple
        # [(key, value), (key2,value2), ... ] 이렇게나옴
        # 여기에 대해서 key가 동일한지 체크해서 뽑아야함
        return self.items[index].get(key)