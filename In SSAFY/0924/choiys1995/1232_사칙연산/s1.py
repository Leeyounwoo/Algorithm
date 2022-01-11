import sys
sys.stdin = open("input.txt")

def calc(v):
    if len(tree[v]) == 2:
        return tree[v][1]
    else:
        L = calc(tree[v][2])
        R = calc(tree[v][3])

        if tree[v][1] == '+':
            return L + R
        elif tree[v][1] == '-':
            return L - R
        elif tree[v][1] == '*':
            return L * R
        else:
            return L / R

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)

    for i in range(1, N+1):
        tmp = input().split()
        tree [int(tmp[0])] = tmp

        # tmp 길이가 4일때, 0번: 정점번호 1번: 연산자, 2번: 왼쪽자식, 3번: 오른쪽자식
        if len(tmp) == 4:
            tree[int(tmp[0])][2] = int(tree[int(tmp[0])][2])
            tree[int(tmp[0])][3] = int(tree[int(tmp[0])][3])
        else:
            tree[int(tmp[0])][1] = int(tree[int(tmp[0])][1])


    print("#{} {}".format(tc, int(calc(1))))