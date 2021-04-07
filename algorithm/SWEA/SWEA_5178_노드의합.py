# 노드의 합
# 완전 이진 트리
for tc in range(int(input())):
    # N: 노드의 개수 M: 리프노드의 개수 L: 출력할 노드 번호
    N, M, L = map(int, input().split())

    # 완전이진트리 초기화 N개 노드이므로
    tree = [-1] * (N+1)
    for n in range(M):
        i, j = map(int, input().split())
        tree[i] = j

    # 노드의 합이 부모 노드의 값이 되므로 후위순회한다
    def postorder_traverse(root):
        global tree
        if root <= N and tree[root] == -1:
            postorder_traverse(root * 2)
            postorder_traverse(root * 2 + 1)
            # 왼쪽자식 노드만 있는 경우 분리하여 처리
            if root * 2 + 1 > N:
                tree[root] = tree[root * 2]
            else:
                tree[root] = tree[root * 2] + tree[root * 2 + 1]
        return tree

    postorder_traverse(1)
    print('#{} {}'.format(tc+1, tree[L]))