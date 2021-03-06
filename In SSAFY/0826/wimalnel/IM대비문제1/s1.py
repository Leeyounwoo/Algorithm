import sys
sys.stdin = open('input.txt')

T = int(input())  #SS텔레콤에서 nxn 배열 기지국

for tc in range(1, T+1):
    N = int(input())
    house = [list(input()) for _ in range(N)]
    count = 0
    # 집이 위치한 원소는 H , 기지국은 A , B , C  아무것도 없는건 X
    for i in range(N):
        for j in range(N):
            if house[i][j] in 'ABC':
                if house[i][j] == 'A':
                    n = 1
                elif house[i][j] == 'B':
                    n = 2
                else:
                    n = 3
                for k in range(1, 1 + n):
                    if -1 < i + k < N and house[i + k][j] == 'H':  # 남
                        house[i + k][j] = 'X'
                    if -1 < i - k < N and house[i - k][j] == 'H':  # 북
                        house[i - k][j] = 'X'
                    if -1 < j + k < N and house[i][j + k] == 'H':  # 동
                        house[i][j + k] = 'X'
                    if -1 < j - k < N and house[i][j - k] == 'H':  # 서
                        house[i][j - k] = 'X'

    cnt = 0
    for i in range(N):
        cnt += house[i].count('H')
    print('#{} {}'.format(tc, cnt))