array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    # 이 부분을 채워보세요!
    array1_inx = 0
    array2_inx = 0
    array1.sort()
    array2.sort()
    n = len(array1)
    m = len(array2)

    result_array = list()
    while array1_inx < len(array1) and array2_inx < len(array2):
        if array1[array1_inx] < array2[array2_inx]:
            result_array.append(array1[array1_inx])
            array1_inx += 1
        else:
            result_array.append(array2[array2_inx])
            array2_inx += 1

    if array1_inx == len(array1):
        for i in range(array2_inx, len(array2)-1):
            result_array.append(array2[i])
    else:
        for i in range(array1_inx, len(array1) - 1):
            result_array.append(array1[i])

    return result_array


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
