input = "abaedcabcad"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    string = string.lower()  # 소문자로 먼저 만들고 시작
    char_array = [0] * 26
    for elem in string:
        char_array[ord(elem) - ord('a')] += 1

    for k, v in enumerate(char_array):
        if v == 1:
            return chr(k + ord('a'))  # 알파벳 순서대로 저장하기 떄문에 이미 순차적으로 구현되어 있으므로 리턴하면 됨

    return "_"


result = find_not_repeating_character(input)
print(result)
