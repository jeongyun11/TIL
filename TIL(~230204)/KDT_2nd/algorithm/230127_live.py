# 다 순환을 하면 for-else문으로 출력

# 의도가 불순하다? 누가?

# 혁신은 죽음에서 발생한다 -> 세대의 변화

# ----------------------------------------

# 힙과 셋

# 힙
# 우선순위 큐

# 힙은 트리형태로 관리

import heapq

N = int(input())
heap = []

for _ in range(N) : 
    n = int(input())
    if n != 0 :
        heapq.heappush(heap, n)

    else :
        if heap :
            print(heapq.heappop(heap))
        else :
            print(0)
# 이진트리

# 작은 값을 출력하고 그 값을 배열에서 제거한다.

# 0아니면 heap push 0아니면 heappop

# 튜플도 가능하다.

# setlen(set(words) 랑 S랑 겹치는 거)

# 자료구조