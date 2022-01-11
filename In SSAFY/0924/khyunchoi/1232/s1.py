import sys
sys.stdin = open('input.txt')


def calc(v):
    if len(tree[v]) == 2:
        return tree[v][1]
    else:
        L = calc(tree[v][2])
        R = calc(tree[v][3])

        if tree[v][1] == '+':
            return L+R
        elif tree[v][1] == '-':
            return L-R
        elif tree[v][1] == '*':
            return L*R
        elif tree[v][1] == '/':
            return L/R


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]

    for i in range(1, N+1):
        tmp = input().split()
        tree[int(tmp[0])] = tmp

        if len(tree[i]) == 4:
            tree[int(tmp[0])][2] = int(tree[int(tmp[0])][2])
            tree[int(tmp[0])][3] = int(tree[int(tmp[0])][3])
        else:
            tree[int(tmp[0])][1] = int(tree[int(tmp[0])][1])

    print('#{} {}'.format(tc, int(calc(1))))
