import math
import itertools


def Solution():
    TestCase = int(input())  # TestCase

    for i in range(0, TestCase):
        inputCondition = str(input())
        chargeStationList = list()  # 충전기가 존재하는 정류장 리스트
        ans: int  # 최소 충전횟수 또는 0
        ans = 0  # 초기값을 0으로 설정

        K = int(inputCondition.split()[0])  # 한 번 충전으로 최대 이동 가능한 정류장 수
        N = int(inputCondition.split()[1])  # 정류장 종점 번호 (0~N)
        M = int(inputCondition.split()[2])  # 충전기가 존재하는 정류장 갯수
        inputData = str(input())
        chargeStationList = list(map(int, inputData.split()))

        ans = maxDistanceToGo(K, N, M, chargeStationList)
        print("#" + str(i + 1) + " " + str(ans))


def maxDistanceToGo(K: int, N: int, M: int, chargeStationList: list()):
    startPoint: int  # 처음에는 0
    startPoint = 0

    prevStartPoint: int
    # 시작위치 설정하는 로직
    # 현재 위치에서 K만큼 더한 값이 chargeStationList 내 값으로 포함되어 있을 경우
    # 현재 위치는 현재 위치에서 K만큼 더한 값으로 바뀌게 된다.
    ansCount: int
    ansCount = 0  # 최종값
    for i in range(0, N):
        if (N - K) <= startPoint and startPoint <= N:
            break
        # startPoint = startPoint + K
        # 초기화할 시작위치(변경 전)
        prevStartPoint = startPoint
        for j in range(K, 0, -1):
            startPoint = prevStartPoint + j
            # j를 다구해서 작업했음에도 현재위치가 다음위치가 되지 않은 경우 갈 수 없음으로 판단하여 0을 반환
            if startPoint in chargeStationList:
                ansCount = ansCount + 1
                break
            else:
                startPoint = prevStartPoint

    # print("마지막 현재위치 : " + str(startPoint))
    # 다했는데도 현재 위치가 종점이 아닌경우 0출력
    if (N - K) <= startPoint and startPoint <= N:
        return ansCount
    else:
        return 0
