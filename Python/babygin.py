import itertools

arrList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def Solution():
    # 0~9 10개의 숫자로 6자리를 뽑아서 앞에 3자리가 RUN/TRIPLETE 확인 뒤에 3자리가 RUN/TRIPLETE 확인
    # 10개의 숫자로 6개의 자리를 만드는 방법 > Permutation (10P6)
    # 10x9x8x7x6x5 만큼의 경우의 수가 나오고 여기서 앞에 3자리 뒤에 3자리 나눠서 RUN, Triplete 조건 확인을 진행할 것
    # ㄱ. 앞의 3자리가 RUN이나 Triplete인 경우 N = 1
    # ㄴ. 뒤의 3자리가 RUN이나 Triplete인 경우 N = 1
    # ㄷ. N의 합이 2가 되는 경우 BabyGIN
    newStrList = itertools.product(arrList,repeat= 6)

    answer: int
    for ans in newStrList:
        answer = isBabyGin(0, ans)
        if answer == 2:
            print(ans)
            print("BabyGIN 입니다.")




def isBabyGin(N: int, strData: str):
    # print(strData[0] + "/" +strData[1] + "/" + strData[2])
    # Triplete
    if int(strData[0]) == int(strData[1]) == int(strData[2]):
        N = N + 1
    elif (int(strData[0]) + 1) == int(strData[1]) and (int(strData[1]) + 1) == int(strData[2]):  # run
        N = N + 1
    if int(strData[3]) == int(strData[4]) == int(strData[5]):  # triplete
        N = N + 1
    elif (int(strData[3]) + 1) == int(strData[4]) and (int(strData[4]) + 1) == int(strData[5]):  # run
        N = N + 1
    return N
