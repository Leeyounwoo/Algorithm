import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while N > 1:
        if N % 2 == 0:
            N = N // 2
            a += 1
        if N % 3 == 0:
            N = N // 3
            b += 1
        if N % 5 == 0:
            N = N // 5
            c += 1
        if N % 7 == 0:
            N = N // 7
            d += 1
        if N % 11 == 0:
            N = N // 11
            e += 1
    print('#{} {} {} {} {} {}'.format(tc+1, a, b, c, d, e))