s = "(())()"


def is_correct_parenthesis(string):
    # 구현해보세요!
    stack = []
    # 바로 직전에 조회한 괄호를 저장해야한다.

    if string[0] == ")":
        return False
    for elem in string:
        if elem == "(":
            stack.append(elem)
        else:
            stack.pop()

    if stack:
        return False
    return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
