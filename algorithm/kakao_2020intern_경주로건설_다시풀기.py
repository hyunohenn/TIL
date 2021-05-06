# 경주로 건설
# 직선과 코너를 골라내는 것이 관건

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = []
route = []
N = 0
min_price = 9999999
min_dist = 99999999

def solution(board):
    global delta, visited, totals, route, N, min_dist, min_price
    # dfs로 경로 찾기
    #delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    N = len(board)
    visited = [[0] * (N) for _ in range(N)]
    visited[0][0] = 1
    #totals = []
    #route = []

    def dfs(r, c, dist):
        global delta, visited, totals, route, N, min_dist, min_price

        dist += 1

        if r == N-1 and c == N-1:
            whole_route = [(0, 0)] + route
            price = find_coner(whole_route)
            if min_price > price:
                min_dist = dist
                min_price = price
            #totals.append(find_coner(whole_route))
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
                if find_coner([(0, 0)]+route) <= min_price and dist <= min_dist:
                    dfs(nr, nc, dist)
                visited[nr][nc] = 0
                route.pop()

    dfs(0, 0, 0)

    answer = min_price

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

board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(board))