import sys
sys.stdin = open('input.txt')

# 단방향 간선 = 유향 간선
# 최단 거리 -> 다익스트라

# 다익스트라 함수 만드는 것부터 해보기

T = int(input())
for tc in range(1,T+1):
    N, M, X = map(int, input().split()) # 사람수, 간선수, 생일파티집

    adj1 = [[987654321] * (N+1) for _ in range(N+1)] # 원래입력 (진출)
    adj2 = [[987654321] * (N+1) for _ in range(N+1)] # 뒤집은입력 (진입)

    for _ in range(M) :
        x, y, c = map(int, input().split()) #c 가중치
        adj1[x][y] = c
        adj2[y][x] = c
    dist1 = [987654321] * (N+1)
    dist2 = [987654321] * (N+1)

    # 다익스트라 호출
    max_value = 0

    for i in range(1, N+1):
        if dist1[i] + dist2[i] > max_value:
            max_value = dist1[i] + dist2[i]

    print('#{} {}'.format(tc, max_value))