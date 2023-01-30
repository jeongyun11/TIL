# 2161. 
from collections import deque

N = int(input())
cards_dq = deque(range(1, N+1))
cards2 = [] #추가만 된다

while True :
    cards2.append(cards_dq.popleft())
    if len(cards_dq) == 0 :
        break
    cards_dq.append(cards_dq.popleft())

print(*cards2)
# =================================
# N = int(input())
# # cards = list(range(1,N + 1))
# cards = [i for i in range(1, N + 1)]
# cards2 = []

# while True :
#     cards2.append(cards.pop(0))
#     if len(cards) == 0 :
#         break
#     cards.append(cards.pop(0))

# print(*cards2)
# =================================
# from collections import deque

# N = int(input())
# cards_dq = deque(range(1, N+1))
# cards2 = [] #추가만 된다

# while len(cards_dq) > 1 :
#     cards2.append(cards_dq.popleft())
#     cards_dq.append(cards_dq.popleft())

# print(*cards2, *cards_dq)