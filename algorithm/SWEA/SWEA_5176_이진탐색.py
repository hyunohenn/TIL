# 이진탐색
# 저장된 값 왼족 서브트리의 루트 < 현재노드 < 오른쪽 서브 트리의 루트
# 중위탐색

# 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값, N/2번 노드에 저장된 값을 출력

for tc in range(int(input())):
    N = int(input())

    # 완전 이진트리이므로 N개의 노드
    tree = [-1] * (N+1)
    num = 1

    # 비어있는 트리를 중위순회하면서 채운다
    def inorder_tree(root):
        global tree, num
        if root <= N and tree[root] == -1:
            inorder_tree(root * 2)
            tree[root] = num
            num += 1
            inorder_tree(root * 2 + 1)
        return tree

    inorder_tree(1)
    print('#{} {} {}'.format(tc+1, tree[1], tree[N//2]))