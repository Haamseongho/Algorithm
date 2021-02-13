import itertools
import math

def Solution():
    N: int
    T = int(input("테스트 수행횟수 입력:"))  # 갯수
    for i in range(0, T):
        N = int(input("입력데이터: "))
        sData = str(input("값 추가 \n"))
        ans = math.trunc(sortMaxMin(sData, N))
        print(ans)


def sortMaxMin(inputData: str, N: int):
    maxNumber : float
    minNumber : float
    maxNumber = float(inputData.split(' ')[0])
    minNumber = float(inputData.split(' ')[0])
    for i in range(0, N):
        if maxNumber < float(inputData.split(' ')[i]):
            maxNumber = float(inputData.split(' ')[i])
        if minNumber > float(inputData.split(' ')[i]):
            minNumber = float(inputData.split(' ')[i])

    return (float(str(maxNumber)) - float(str(minNumber)))
    # ans = int(max(float(inputData)) - min(float(inputData)))
    # return ans