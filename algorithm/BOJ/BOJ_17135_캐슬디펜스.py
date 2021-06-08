# 캐슬디펜스
# 오호 완전 헬름협곡의 전투

N, M, D = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
# N+1 성이 있는 라인

from itertools import combinations
tmp = [i for i in range(N)]
archer = list(combinations(tmp, 3))

