# 메모이제이션 이용
import sys
sys.stdin = open('input.txt')

def paper(n):
    lst = [1, 3]

    for i in range(2, n):
        lst.append(lst[i-1] + lst[i-2]*2)

    return lst[n-1]

T = int(input())

for tc in range(T):
    n = int(input())
    print('#{0} {1}'.format(tc+1, paper(n//10)))