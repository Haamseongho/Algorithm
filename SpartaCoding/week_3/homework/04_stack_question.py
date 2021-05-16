from collections import deque
N: int = 8


def Solution(count: int):
    stack_number = []  # list
    sequential_number = []
    for i in range(count):
        n = int(input())
        stack_number.append(n)  # 순차적으로 입력값 기입

    for i in range(count):
        sequential_number.append(i)

    while len(stack_number) <= count:

        while len(sequential_number) <= count:



a = int(input())
print(Solution(a))
