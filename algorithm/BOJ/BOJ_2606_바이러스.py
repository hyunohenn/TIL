# 바이러스
# 이거 상호 배타 집합 결국에 findset[x] == 1 인 모든 경우의 수 찾기

# make_set
def make_set():
    for i in range(V+1):
        p[i] = i

# find_set
def find_set(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]


# 합치자
def union_set(x, y):
    target = find_set(y)
    new_leader = find_set(x)
    for i in range(len(p)):
        if p[i] == target:
            p[i] = new_leader


V = int(input())
E = int(input())  # 컴퓨터의 수는 1부터 차례로 번호, E는 네트워크 쌍의 수
adj = [[] for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


p = [0] * (V+1)

make_set()


cnt = 0
for i in range(V+1):
    if len(adj[i]):
        for j in range(len(adj[i])):
            union_set(i, adj[i][j])

# 여기가 다름
print(p.count(find_set(1))-1)   # 웜 바이러스를 통해 바이러스에 걸리게 되는 컴퓨터의 수니까 -1
