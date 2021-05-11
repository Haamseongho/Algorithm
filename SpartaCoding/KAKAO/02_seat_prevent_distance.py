vx = [-1, 0, 1, 0]
vy = [0, -1, 0, 1]


def find_place(x, y, places, visited, count):
    if count >= 24:
        return 1

    print(x, y, places[x][y])

    for i in range(4):
        dx = x + vx[i]
        dy = y + vy[i]
        if dx >= 0 and dx < 5 and dy >= 0 and dy < 5:
            if visited[dx][dy] == False:
                print(places[dx][dy])
                if places[dx][dy] == "P":
                    visited[dx][dy] = True
                    return 0
                elif places[dx][dy] == "O":
                    visited[dx][dy] = True
                    # i의 값에 따라 체크 방향이 달라짐
                    if i == 0:
                        if dy - 1 >= 0 and dy + 1 < 5:
                            if places[dx][dy - 1] == "P" or places[dx][dy + 1] == "P":
                                return 0
                    elif i == 1:
                        if dx - 1 >= 0 and dx + 1 < 5:
                            if places[dx - 1][dy] == "P" or places[dx + 1][dy] == "P":
                                return 0
                    elif i == 2:
                        if dy - 1 >= 0 and dy + 1 < 5:
                            if places[dx][dy - 1] == "P" or places[dx][dy + 1] == "P":
                                return 0
                    else:
                        if dx - 1 >= 0 and dx + 1 < 5:
                            if places[dx - 1][dy] == "P" or places[dx + 1][dy] == "P":
                                return 0
                else:  # "X" 인 곳도 우선 감
                    visited[dx][dy] = True
                find_place(dx, dy, places[dx][dy], visited, count + 1)


def solution():
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    visited = [[False] * 5] * 5
    # 1. P 동서남북 모두 P가 되면 안됨 --> P가 하나라도 있으면 0
    # 2. P 동서남북으로 모두 P가 없는 경우
    # 3. P 대각선 방향에 P가 있는지 찾기 : 있으면 해당 P와 기존 P에 인접한 방향에
    # O인지 X인지 체크 > O면 0
    answer = []
    for i in range(len(places)):
        print(places[i])
        find_place(0, 0, places[i], visited, 0)
        # for j in range(len(places[i])):

            # count = find_place(i, j, places[i][j], visited, 0)
        #answer.append(count)
    #return answer


print(solution())
