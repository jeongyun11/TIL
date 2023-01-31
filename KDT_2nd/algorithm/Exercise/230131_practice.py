import sys
sys.stdin = open('test.txt', 'r')


# # 2441. 
# N = int(input())

# for n in range(N) :
#     print(' '*n + '*'*(N-n))


# # 2592.

# numbers = [int(input()) for i in range(10)]
# numbers_dict = {}
# for number in numbers :
#     numbers_dict[number] = numbers_dict.get(number,0) + 1

# print(round(sum(numbers)/len(numbers)))
# print(sorted(numbers_dict.items(), key = lambda x : x[1], reverse=True)[0][0])


# # 10798.
# words = [list(input()) for i in range(5)]
# Y = 5
# X = len(max(words,key=len))

# for y in range(Y) :
#     if len(words[y]) < X :
#         for i in range(X - len(words[y])) :
#             words[y].append(None)


# for x in range(X) :
#     for y in range(Y) :
#         if words[y][x] == None :
#             continue
#         print(words[y][x], end='')


# 9455.
# x와 y 대칭
T = int(input())
for t in range(T) :
    X, Y = map(int, input().split())
    matrix = [list(map(int, input().split())) for x in range(X)]
    matrix_2 = [[0 for x in range(X)] for y in range(Y)]

    cnt = 0
    for x in range(X) :
        for y in range(Y) :
            matrix_2[y][x] = matrix[x][y]

    for y in range(Y) :
        for x in range(X) :
            if matrix_2[y][x] == 1 :
                cnt += matrix_2[y][x+1:].count(0)
    print(cnt)

    
# # 1652.
# Y = int(input())
# X = Y


# matrix = [list(input()) for y in range(Y)]

# matrix2 = [[[0] for x in range(X)] for y in range(Y)]
# for y in range(Y) :
#     for x in range(X) :
#         matrix2[y][x] = matrix[x][y]

# result1, result2 = 0, 0

# for y in range(Y) :
#     matrix[y].append('X')

# for y in range(Y) :
#     cnt = 0
#     for x in range(X+1) :
#         if matrix[y][x] == '.' :
#             cnt +=1
            
#         else :
#             if cnt >= 2 :
#                 result1 += 1
#             cnt = 0
        

# for y in range(Y) :
#     matrix2[y].append('X')

# for y in range(Y) :
#     cnt = 0
#     for x in range(X+1) :
#         if matrix2[y][x] == '.' :
#             cnt +=1
#         else :
#             if cnt >= 2 :
#                 result2 += 1
#             cnt = 0
        
# print(result1, result2)


# # 2775. 
# T = int(input())

# for _ in range(T) :
#     K = int(input())
#     N = int(input())

#     floor = [i for i in range(1, N + 1)]

#     for k in range(K) :
#         for n in range(N - 1,-1, -1) :
#             floor[n] = sum(floor[:n+1])

#     print(floor[-1])