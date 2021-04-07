# 이진 힙
# 이진 최소힙 특징
# 1. 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드 추가
# 2. 부모 노드의 값 < 자식 노드의 값
# 3. 노드 번호 차례로

for tc in range(int(input())):
    N = int(input())  # 노드의 개수
    tmp = list(map(int, input().split()))
    # 힙초기화
    heap = [-1] * (N+1)

    # 최소힙 순서대로 값 삽입
    last = 0
    for n in tmp:
        last += 1
        heap[last] = n
        position = last
        # 힙 조건 체크
        while position != 1 and heap[position//2] > n:  # 루트이거나 부모 노드가 작을 때까지
            # 바꾼다
            heap[position], heap[position // 2] = heap[position // 2], heap[position]
            position = position // 2

    # print(heap)
    # 마지막 노드의 조상 노드의 합
    sum = 0
    last_node_ances = N//2
    while last_node_ances >= 1:
        sum += heap[last_node_ances]
        last_node_ances //= 2
    print('#{} {}'.format(tc+1, sum))
