# import sys
# sys.stdin = open("test.txt","r")

# 10101. count? dict? 
numbers = [int(input()) for i in range(3)]

result = 'Scalene'

if sum(numbers) != 180 :
    result = 'Error'
else  :
    for number in numbers : 
        if numbers.count(number) == 3 :
            result = 'Equilateral'
            break

        elif numbers.count(number) == 2 :
            result = 'Isosceles'
            break

print(result)


# 2720. 
T = int(input())

for t in range(T) :
    money = int(input())
    calcul_list = []

    calcul_list.append(money // 25)
    money = money % 25

    calcul_list.append(money // 10)
    money = money % 10
    
    calcul_list.append(money // 5)
    money = money % 5

    calcul_list.append(money)

    print(*calcul_list)


# 1453. 해시
N = input()
numbers = map(int,input().split())
seat = set()
cnt = 0
for number in numbers :
    if number not in seat :
        seat.add(number)
    else : 
        cnt += 1
print(cnt)


# 10773. 
K = int(input())
numbers = []
for k in range(K) :
    number = int(input())
    if number == 0 :
        numbers.pop()
    else :
        numbers.append(number)

print(sum(numbers))


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


# from collections import deque

# N = int(input())
# cards_dq = deque(range(1, N+1))
# cards2 = [] #추가만 된다

# while len(cards_dq) > 1 :
#     cards2.append(cards_dq.popleft())
#     cards_dq.append(cards_dq.popleft())

# print(*cards2, *cards_dq)


# 9012.
T = int(input())
for t in range(T) :
    PS_str = input()
    PS_list = []
    result = 'YES'

    for ps in PS_str :
        if ps == '(' :
            PS_list.append(ps)
        else : # ')'
            if PS_list :
                PS_list.pop()
            else :
                result = 'NO'
                break
    if PS_list :
        result = 'NO'

    print(result)