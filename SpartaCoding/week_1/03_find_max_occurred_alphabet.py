input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = [0] * 26
    for char in string:
        if char.isalpha():
            index = ord(char) - ord('a')
            alphabet_array[index] += 1

    max_alpha_occurred = alphabet_array[5]
    max_inx = 5
    for inx, alpha in enumerate(alphabet_array):
        if alpha > max_alpha_occurred:
            max_alpha_occurred = alpha
            max_inx = inx

    # 숫자를 알파벳으로 변환
    # 0번째가 a이므로 max_inx에서는 a가 가장 많이 나왔기 떄문에 0이 나오고 0의 인덱스에 ord('a')를 더하면
    # 즉 97을 더하면 a가 나오게 됩니다.
    return max_inx, max_alpha_occurred, chr(max_inx + ord('a'))


result = find_max_occurred_alphabet(input)

print(result)
