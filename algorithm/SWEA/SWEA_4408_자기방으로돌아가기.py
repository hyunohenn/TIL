# 자기 방으로 돌아가기

# 방 번호에 따른 index를 찾아
# 경로 안에서의 인덱스 구간을 찾고
# 구간을 지났다면 +1 을 한 뒤 최대값 구하기

for tc in range(int(input())):
    N = int(input())  # 돌아갈 학생 수

    # 방 리스트 초기화
    route = [0] * 200


    for case in range(N):
        start, end = map(int, input().split())

        # 방 번호가 홀수, 짝수냐에 따라 idx를 다르게 구한다
        if start % 2:
            start_idx = start//2
        else:
            start_idx = start//2 - 1

        if end % 2:
            end_idx = end//2
        else:
            end_idx = end//2 - 1


        # 출발 지점과 도착 지점 구간의 idx에 +1
        if start_idx <= end_idx:
            for r in range(start_idx, end_idx+1):
                route[r] += 1

        if end_idx < start_idx:
            for r in range(end_idx, start_idx+1):
                route[r] += 1


    print('#{} {}'.format(tc+1, max(route)))