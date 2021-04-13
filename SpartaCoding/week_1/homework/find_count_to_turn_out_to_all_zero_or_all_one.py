input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    # 1101010
    # 0001010
    # 0000010
    # 0000000

    # 1111010
    # 1111110
    # 1111111
    zero_to_one_count = 0
    one_to_zero_count = 0
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i+1] == '0':
                zero_to_one_count += 1
            elif string[i+1] == '1':
                one_to_zero_count += 1

    return min(one_to_zero_count, zero_to_one_count)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
