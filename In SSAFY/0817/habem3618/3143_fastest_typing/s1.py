import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    n = A.count(B)

    print("#{} {}".format(tc, len(A) - (n*len(B)) + n))
