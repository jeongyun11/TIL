# # import sys
# # sys.stdin = open('test.txt','r')

# # 1225.
# n, m = input().split()
# print(sum(map(int,list(n))) * sum(map(int,list(m))))


# # 2438.
# N = int(input())
# for n in range(1,N + 1) :
#     print('*' * n)


# # 2739.
# N = int(input())

# for i in range(1, 10) :
#     print(f'{N} * {i} = {N * i}')


# # 2953.
# score = []
# for i in range(5) :
#     score.append(sum(map(int, input().split())))

# for i in range(5) :
#     if max(score) == score[i] :
#         print(i + 1, score[i])


# # 2669.
# set_point = set()

# for _ in range(4) :
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(x1, x2) :
#         for j in range(y1, y2) :
#             set_point.add((i,j))

# print(len(set_point))


a,b = input().split()
a_l = list(map(int,a))
print(a_l)