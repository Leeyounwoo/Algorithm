import sys
sys.stdin = open('input.txt')

def merge(lst):
    cnt = 0
    len_lst = len(lst)
    if len_lst <= 1:
        return lst, cnt
    else:
        # 분리
        left, left_cnt = merge(lst[: len_lst // 2])
        right, right_cnt = merge(lst[len_lst // 2:])

        # 리스트 병합
        result = []  # 리턴 할 리스트
        left_idx = right_idx = 0  # 좌우측 인덱스
        right_is_small = False
        for _ in range(len_lst):
            if left_idx == len(left):  # 좌측 리스트가 없다면
                result.append(right[right_idx])  # 우측 리스트에서 가져옴
                right_idx += 1

            elif right_idx == len(right):  # 우측 리스트가 없다면
                result.append(left[left_idx])  # 좌측 리스트에서 가져옴
                left_idx += 1
                right_is_small = True  # 오른쪽 마지막 원소가 작은 경우

            elif left[left_idx] <= right[right_idx]:  # 좌측 리스트의 값이 작을 때
                result.append(left[left_idx])  # 좌측 리스트에서 가져옴
                left_idx += 1

            else:  # 우측 리스트의 값이 작을 때
                result.append(right[right_idx])  # 우측 리스트에서 가져옴
                right_idx += 1

        # cnt 계산
        cnt = left_cnt + right_cnt
        if right_is_small:  # 오른쪽 마지막 원소가 작은 경우
            cnt += 1

        return result, cnt


def sorted_merge(lst):
    sorted_lst, cnt = merge(lst)
    return sorted_lst[N // 2], cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    print('#{}'.format(tc), *sorted_merge(lst))