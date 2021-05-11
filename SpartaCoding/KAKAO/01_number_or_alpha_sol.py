data = "one4seveneight"
def solution(s):
    if s == 0 or s == 'zero':
        return

    number_alpha_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    number_dict = {}
    for number in range(0, 9):
        number_dict[number_alpha_list[number]] = number

    ans = ""
    check_string = ""
    answer: int = 0
    for s_text in s:
        if s_text.isdigit():
            ans = ans + str(s_text)
            check_string = ""
        else:
            check_string = check_string + s_text

        if len(check_string) >= 3:
            for i in range(0, 9):
                if number_alpha_list[i] == check_string:
                    ans = ans + str(number_dict[number_alpha_list[i]])
                    check_string = ""
                    break

    answer = ans[0] * 1000 + ans[1] * 100 + ans[2] * 10
    return answer

print(solution(data))