import sys
sys.stdin = open('input.txt')

def div(num) :
    return (int(num) + 1) // 2

T = int(input())
for tc in range(1, T + 1): # 1,2,3
    N = int(input())

    students = [list(map(int, input().split())) for _ in range(N)]
    road = [0] * 201

    for i in range(N) :
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]

        for j in range(students[i][0], students[i][1]+1) :
            road[j] += 1
    print('#{} {}'.format(tc, max(road)))
