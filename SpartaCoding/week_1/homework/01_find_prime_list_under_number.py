input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    # 소수 : 소인수분해 했을때 1 또는 자기자신
    ans = []

    for i in range(2, number):
        value = i
        ans.append(value)
        for j in range(2, i - 1):
            if (i % j) == 0:
                ans.remove(value)
                break

    return ans


result = find_prime_list_under_number(input)
print(result)
