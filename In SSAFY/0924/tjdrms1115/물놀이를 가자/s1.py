import sys
sys.stdin = open('input.txt')
from collections import deque


# def is_border(N, M, i, j):
#     if (0 <= i < N) and (0 <= j < M):
#         return True
#     return False


T = int(input())

delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
answer = []
for tc in range(1, T + 1):

    N, M = map(int, input().split())

    board = [list(input()) for _ in range(N)]

    visited = [[-1 for _ in range(M)] for _ in range(N)]

    queue = deque()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'W':
                # i, j, distance
                visited[i][j] = 0
                # queue.append((i, j, 0))
                queue.append((i, j))

    result = 0
    while queue:
        # i, j, d = queue.pop(0)
        # i, j, d = queue.popleft()
        i, j = queue.popleft()
        d = visited[i][j]
        result += d
        # for di, dj in delta:
        for a in range(4):
            di, dj = delta[a][0], delta[a][1]
            # if is_border(N, M, i + di, j + dj) and not visited[i + di][j + dj]:
            if (0 <= i + di < N) and (0 <= j + dj < M) and (visited[i + di][j + dj] == -1):
                visited[i+di][j+dj] = d + 1
                # queue.append((i + di, j + dj, d + 1))
                queue.append((i + di, j + dj))

    # for i in range(N):
        # for j in range(M):
        #     result += visited[i][j] - 1

    # result -= N*M
    # print(f'#{tc} {result}')
    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')

