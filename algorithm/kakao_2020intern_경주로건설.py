# 경주로 건설
# 직선과 코너를 골라내는 것이 관건

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = []
route = []
N = 0
min_dist = 9999999

# 앞으로 갈 방향/ 가격을 포함한 경로도 중복 체크 해줘야함
def solution(board):
    global delta, visited, totals, route, N, min_dist
    # dfs로 경로 찾기
    N = len(board)
    visited = [[0] * (N) for _ in range(N)]
    visited[0][0] = 1

    def dfs(r, c):
        global delta, visited, totals, route, N, min_dist
        if r == N-1 and c == N-1:
            whole_route = [(0, 0)] + route
            dist = find_coner(whole_route)
            if min_dist > dist:
                min_dist = dist

        else:
            for d in range(4):
                nr = r + delta[d][0]
                nc = c + delta[d][1]
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if board[nr][nc] == 1:
                    continue
                if visited[nr][nc] == 1:
                    continue
                visited[nr][nc] = 1
                route.append((nr, nc))
                if find_coner([(0, 0)]+route) <= min_dist:
                    dfs(nr, nc)
                visited[nr][nc] = 0
                route.pop()

    dfs(0, 0)
    answer = min_dist
    return answer

# 직선과 코너 골라내는 함수
# 찾아낸 길의 경로를 담고있는 리스트를 받아서
# 경로의 경우 시작과 끝점을 제외하고 양 옆의 좌표가 r, c 둘 다 다르면 무조건 코너
# 예를 들면
# 00 - 10 - 11 - 12 - 23 이면
# 직   코    직    코   직
def find_coner(path_list):
    total_price = 100  # 기본적으로 처음과 끝 점은 무조건 직선이므로
    for i in range(1, len(path_list)-1):
        if path_list[i-1][0] != path_list[i+1][0] and path_list[i-1][1] != path_list[i+1][1]:
            # 코너임
            total_price += 600
        else:
            total_price += 100
    return total_price

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))