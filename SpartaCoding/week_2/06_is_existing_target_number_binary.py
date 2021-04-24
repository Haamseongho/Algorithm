finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    array.sort()
    s_inx = 0
    e_inx = len(array) - 1
    m_inx = (s_inx + e_inx) // 2

    mid = array[m_inx]
    while s_inx <= e_inx:
        if array[m_inx] == target:
            return True
        elif array[m_inx] < target:
            s_inx = m_inx + 1
        else:
            e_inx = m_inx - 1
        m_inx = (s_inx + e_inx) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
