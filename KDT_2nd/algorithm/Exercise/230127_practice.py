# import sys
# sys.stdin = open('test.txt', 'r', encoding='utf-8')
import heapq

# 10817.
numbers = list(map(int, input().split()))
# max = numbers[0]
# index = 0
# for i in range(1,len(numbers)) :
#     if numbers[i -1] < numbers[i] :
#         max = numbers[i]
#         index = i
# numbers.pop(index)
# print(max(numbers))

heapq.heapify(numbers)
heapq.heappop(numbers)
print(heapq.heappop(numbers))

# 정렬하고 index 2 출력


# 20001. cnt or append&pop
start = input()
duck = str()
list_duck = []
cnt = 0
while True :
    duck = input()
    if duck == '고무오리 디버깅 끝' :
        break

    if duck == '문제' :
        cnt += 1
    else : # 고무오리 
        if cnt == 0 :
            cnt += 2
        else :
            cnt -= 1

if cnt == 0 :
    print('고무오리야 사랑해')
else :
    print('힝구')

# 1269.
x,y = input().split()
A = set(map(int,input().split()))
B = set(map(int,input().split()))
print(len(A^B))


# 3052.
numbers = set((int(input()) % 42) for i in range(10))

print(len(numbers))


# 1181.
import sys
# N = int(sys.stdin.readline())
# words = set(sys.stdin.readline().rstrip() for i in range(N))
N = int(input())
words = set(input().rstrip() for i in range(N))
dict_len = {}

for word in words :
    if len(word) not in dict_len :
        dict_len[len(word)] = []
    # else :
    dict_len[len(word)].append(word)

for i in sorted(dict_len) :
    print(*sorted(dict_len[i]), sep='\n')

# for i in sorted(dict_len.items()) :
#     print(*sorted(i[1]), sep='\n')

# # 11286
import sys
import heapq
input = sys.stdin.readline
N = int(input())
numbers = []
# # for n in range(N) :
# #     number = int(input())
# #     if number != 0 :
# #         numbers.append(((number * -1) if number < 0 else number, number))
# #         sorted(numbers,)
# #     elif len(numbers) == 1:
# #         print(numbers.pop())
# #     elif len(numbers) == 0:
# #         print(0)
# #     elif numbers[-1] < numbers[-2]:
# #         print(numbers.pop())
# #     else :
# #         print(numbers.pop(-2))

for n in range(N) :
    number = int(input())
    if number != 0 :
        heapq.heappush(numbers, ((number * -1) if number < 0 else number, number))
    else : # 0이면 남아있을때 없을때
        if numbers : 
            print(heapq.heappop(numbers)[1])
        else : 
                print(0)