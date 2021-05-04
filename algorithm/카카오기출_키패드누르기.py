def solution(numbers, hand):
    answer = ""
    # 초기화 값
    num_l = 10
    num_r = 12
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'

        # 현재 위치가 같을 때
        elif num_l == num:
            answer += 'L'

        elif num_r == num:
            answer += 'R'

        else:
            answer += find_dist(num_l, num_r, num, hand)

        # 결정 뒤 현재 손이 있는 위치 갱신
        if answer[-1] == 'L':
            num_l = num
        else:
            num_r = num

    return answer


# 각 숫자에 맞는 좌표값 array 만들기
xy = [[] for _ in range(13)]
for key in range(1, 13):
    xy[key] = [(key-1) // 3, (key-1) % 3]  # 1부터 시작하기 때문에 -1
xy[0] = [3, 1]



# 손 위치와 숫자 사이의 거리 찾는 함수(BFS)
def find_dist(num_l, num_r, num, hand):
    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dists = []  # 0: 왼손, 1: 오른손

    # num의 좌표
    target_i, target_j = xy[num][0], xy[num][1]

    # 현재 손이 있는 위치
    left_i, left_j = xy[num_l][0], xy[num_l][1]
    right_i, right_j = xy[num_r][0], xy[num_r][1]

    for one_hand in range(2):
        if one_hand == 0:
            start_i, start_j = left_i, left_j
        else:
            start_i, start_j = right_i, right_j

        min_dis = 9999999
        visited = [[0] * 3 for _ in range(4)]
        q = []
        dis = 0
        q.append((start_i, start_j, dis))
        visited[start_i][start_j] = 1

        while q:
            i, j, dis = q.pop(0)
            dis += 1

            for d in range(4):
                ni = i + delta[d][0]
                nj = j + delta[d][1]

                if 0<= ni < 4 and 0<= nj < 3 and visited[ni][nj] == 0 and dis <= min_dis:
                    q.append((ni, nj, dis))
                    visited[ni][nj] = 1

                    if ni == target_i and nj == target_j:
                        if dis < min_dis:
                            min_dis = dis
        dists.append(min_dis)

    if dists[0] < dists[1]:
        return 'L'
    elif dists[0] > dists[1]:
        return 'R'
    else:
        if hand == 'right':
            return 'R'
        else:
            return 'L'

