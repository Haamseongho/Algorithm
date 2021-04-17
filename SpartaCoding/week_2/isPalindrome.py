import collections
from typing import Deque


input1: str = "abccba"
input2: str = "aaccbb"

def isPalindrome(s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False  # 앞에서 빼고 뒤에서 빼고 서로 다르면 팰린드롬이 아님

    return True

a = isPalindrome(input1)
print(a)
print(isPalindrome(input2))
