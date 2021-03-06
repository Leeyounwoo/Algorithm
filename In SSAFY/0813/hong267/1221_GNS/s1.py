import sys

sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    tc = input().split()
    num_list = input().split()
    num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5,
                'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    chg_list = []
    for i in range(int(tc[1])):
        chg_list.append(num_dict[num_list[i]])

    for i in range(len(chg_list)-1, 0, -1):
        for j in range(i):
            if chg_list[j] > chg_list[j+1]:
                chg_list[j], chg_list[j+1] = chg_list[j+1], chg_list[j]

    chg_dict = {}
    for k, v in num_dict.items():
        chg_dict[v] = k

    result_list = []
    for i in chg_list:
        result_list.append(chg_dict[i])

    print(tc[0])
    print(' '.join(result_list))
