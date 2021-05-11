def Solution():
    # 1차원 배열 입력
    n = int(input("배열길이 입력"))
    arr = list(map(int, input().split()))  # 1차원 배열

    print(arr)

    length = len(arr)  # 배열길이

    for i in range(1 << length):
        ans = 0
        for j in range(length):
            if i & (1 << j):
                ans = arr[j] + ans
                if ans == 0:
                    print(arr[j])
        print()
