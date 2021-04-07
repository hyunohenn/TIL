# subtree

for tc in range(int(input())):
    E, N = map(int, input().split())
    tmp = list(map(int, input().split()))

    # 노드 번호가 1번부터 E+1번까지 존재하므로
    tree = [[] for _ in range(E+1 + 1)]
    for i in range(0, len(tmp), 2):
        tree[tmp[i]].append(tmp[i+1])

    cnt = 1
    # 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수
    def find_node(root):
        global cnt
        if len(tree[root]) != 0:
            cnt += len(tree[root])
            for i in tree[root]:
                find_node(i)
        return cnt

    print('#{} {}'.format(tc+1, find_node(N)))