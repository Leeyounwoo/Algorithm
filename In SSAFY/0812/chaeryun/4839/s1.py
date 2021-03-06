import sys
sys.stdin = open("input.txt")

T = int(input())

def search(info):
    #  정보 불러오기
    P = info[0]
    print(P)
    Pa = info[1]
    print(Pa)
    Pb = info[2]

    now = 0       # 현재 위치한 페이지

    L = 1         # 왼쪽페이지와 오른쪽 페이지 초기값
    R = P

    count_A = 0    # A와 B의 횟수
    count_B = 0

    while not now == Pa:               # Pa 검사
        center = int((L+R)/2)          # 중앙값
        if Pa > center:                # 중앙값이 어디에 위치하냐에 따라 범위 바꿔줌
            L = center
        else :
            R = center
        now = center         # 현재위치 설정
        count_A += 1         # 횟수 증가

    # 현재 위치한 페이지
    now = 0
    # 왼쪽페이지와 오른쪽 페이지 초기값
    L = 1
    R = P

    # Pb 검사
    while not now == Pb:
        # 중앙값
        center = int((L + R) / 2)
        # 중앙값이 어디에 위치하냐에 따라 범위 바꿔줌
        if Pb > center:
            L = center
        else:
            R = center
        # 현재위치 설정
        now = center
        # 횟수 증가
        count_B += 1

    if count_A < count_B:
        return 'A'
    elif count_A > count_B:
        return 'B'
    else:
        return 0



for tc in range(1, T+1):
    info = list(map(int, input().split()))
    result = search(info)
    print("#{} {}".format(tc,result ))