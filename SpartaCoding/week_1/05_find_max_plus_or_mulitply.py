input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    value = array[0]  # 초기값 (왼쪽 > 오른쪽 순으로 진행)
    for elem in array:
        if elem * value > elem + value:
            value = elem * value
        else:
            value = elem + value

    return value


#
# def find_max_plus_or_multiply(array):
# 이 부분을 채워보세요!
#    multiply_sum = 0
#    for elem in array:
#        if elem <= 1 or multiply_sum <= 1:
#            multiply_sum += elem
#        else:
#           multiply_sum *= elem

#    return multiply_sum
#
result = find_max_plus_or_multiply(input)
print(result)
