import sys
sys.stdin = open('input.txt')
from collections import deque


def merge(left, right):
    global count

    left = deque(left)
    right = deque(right)

    if left[-1] > right[-1]:
        count += 1

    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    ans = merge_sort(arr)

    print("#{} {} {}".format(tc, ans[N // 2], count))
