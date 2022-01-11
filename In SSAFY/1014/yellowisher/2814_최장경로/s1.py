def dfs(i, cnt):
    global edge

    if cnt > edge:
        edge = cnt

    for j in range(1, N + 1):
        if j in arr[i] and not visited[j]:
            visited[j] = 1
            dfs(j, cnt + 1)
            visited[j] = 0

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    edge = 0

    for _ in range(M):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)

    for i in range(1, N + 1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print('#{} {}'.format(t, edge))