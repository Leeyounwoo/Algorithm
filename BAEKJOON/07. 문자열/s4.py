for T in range(int(input())):
    n, s = map(str, input().split())
    n = int(n)
    for i in range(len(s)):
        print(s[i] * n, end='')
    print()