input = [3, 5, 6, 1, 2, 4]
# max_num = 0


def find_max_num(array):
    # 이 부분을 채워보세요!
    # ans = max(input)
    max_num = array[0]
    for num in array:
        if max_num < num:
            max_num = num
    # 숫자 비교를 하는데, break를 한 번도 거치지 않았다면
    # 비교 대상 중 가장 큰 값이라고 판단하고
    # 리턴한다 (else : 안쪽 for문의 반례)
    return max_num


result = find_max_num(input)
print(result)
