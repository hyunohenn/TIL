# 하노이 탑 이동 순서
# 후입선출(LIFO) 방식 -> stack!!!!
# stack.pop() stack.append()

N = int(input())

# 초기화
columns = [[] for _ in range(3)]
for i in range(N, 0, -1):
    columns[0].append(i)

# 경로를 찾는것 -> 최단거리이므로 BFS
# 인접(가능한 경로 찾는 것) 경로 찾기 -> stack

# plate = (현재위치, 원판 번호)
# 가능한 경우의 수 구하기
def find(plate):
    possible = []
    for col in range(3):
        if plate[0] != col:
            if len(columns[col]) == 0 or columns[col][-1] > plate[1]:
                possible.append(col)

    return possible


def BFS(possible):
    q = []
    for p in possible:
        q.append(p)

#################### 다시 풀어볼것
