import sys

sys.stdin = open('input.txt')


def find_num(seq, mult):
    ratio = []
    cur = 0
    count = 0
    for i in range(len(seq)):
        num = int(seq[i])
        if cur ^ num:
            ratio.append(count)
            cur = (~cur) & 1
            count = 1
        else:
            count += 1
    ratio.append(count)

    for i in range(len(ratio)):
        ratio[i] //= mult

    if ratio == [3, 2, 1, 1]:
        return 0
    elif ratio == [2, 2, 2, 1]:
        return 1
    elif ratio == [2, 1, 2, 2]:
        return 2
    elif ratio == [1, 4, 1, 1]:
        return 3
    elif ratio == [1, 1, 3, 2]:
        return 4
    elif ratio == [1, 2, 3, 1]:
        return 5
    elif ratio == [1, 1, 1, 4]:
        return 6
    elif ratio == [1, 3, 1, 2]:
        return 7
    elif ratio == [1, 2, 1, 3]:
        return 8
    elif ratio == [3, 1, 1, 2]:
        return 9
    else:
        return -1


def decode(code, mult):
    bin_code = ''
    length = 56 * mult
    for c in code:
        bin_code += bin(int(c, 16))[2:].zfill(4)
    end = 0
    for i in range(len(bin_code) - 1, -1, -1):
        if bin_code[i] == '1':
            end = i
            break
    if end < length - 1:
        return 0

    bin_code = bin_code[end - length + 1:end + 1]
    checksum = 0
    result = 0
    digit = 1
    for i in range(0, length, 7 * mult):
        num = find_num(bin_code[i:i + (7 * mult)], mult)
        if num == -1:
            return -1

        if digit % 2 == 1:
            checksum += 3 * num
        else:
            checksum += num
        digit += 1
        result += num
    if (checksum % 10) != 0:
        return 0
    else:
        return result


T = int(input())

answer = []
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    result = 0
    code_rec_list = []
    for i in range(N):
        for j in range(M - 1, -1, -1):
            flag = False
            for top, left, bottom, right in code_rec_list:
                if (top <= i <= bottom) and (left <= j <= right):
                    flag = True
                    break
            if flag:
                continue

            if board[i][j] != '0':
                mult = 1
                temp = 0
                while j - (14 * mult) >= 0:
                    code = board[i][j - (14 * mult):j + 1]
                    temp = decode(code, mult)
                    if temp >= 0:
                        break
                    mult += 1
                if temp > 0:
                    result += temp
                left, right = j - (14 * mult), j
                top = i
                bottom = 0
                for k in range(i + 1, N):
                    if board[k][j] != board[i][j]:
                        bottom = k - 1
                        break
                else:
                    bottom = N - 1
                code_rec_list.append((top, left, bottom, right))

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
