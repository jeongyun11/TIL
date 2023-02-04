# import sys
# sys.stdin = open('test.txt','r')

# 2525.
hours, minutes = map(int, input().split())

minutes_add = int(input())
minutes += minutes_add

while minutes >= 60 :
    minutes -= 60
    hours += 1

if hours >= 24 :
    hours -= 24


print(hours, minutes)

# 9076.
N, M = map(int,input().split())
cards = list(map(int,input().split()))
sum_num = set()
list_sum = []
for i in range(N-2) :
    for j in range(i+1, N-1) :
        for k in range(j+1, N) :
            if(cards[i] +cards[j] + cards[k]) <= M :
                sum_num.add(cards[i] +cards[j] + cards[k])
print(sorted(sum_num,reverse=True)[0])

# for i in range(N) : # 겹친다. 숫자의 중복
#     for j in range(i + 1, N) :
#         for k in range(j + 1, N) :
#             if(cards[i] +cards[j] + cards[k]) <= M :
#                 sum_num.add(cards[i] +cards[j] + cards[k])
# print(sorted(sum_num,reverse=True)[0])


# 9076.
T = int(input())

for _ in range(T) :
    scores = list(map(int, input().split()))
    scores.remove(max(scores))
    scores.remove(min(scores))

    if (max(scores) - min(scores)) >= 4 :
        print('KIN')
    else :
        print(sum(scores))


# 1526.
N = input()

if int(N) >= int('4'*(len(N))) :
    result = '7'*(len(N))
else : result = '7'*(len(N)-1)

i = len(result)-1

while int(N) < int(result) :
    if result[i] == '7' :
        result_list = list(result)
        result_list[i] = '4' 

        for j in range(i+1, len(result)) :
            result_list[j] = '7'

        result = ''
        for i in range(len(result_list)) :
            result += result_list[i]
        i = len(result)
    i -= 1        

print(result)

# 1436.
N = int(input())
cnt = 0
number = 666
while cnt < N :

    if '666' in str(number) :
        cnt += 1
    number += 1

print(number - 1)

# combinations

# 박태양님

# #2
# l = input()
# k = ''
# r = ''
# for i in range(len(l)):
#     k += l[i]
#     if int(k)>7:
#         r += '7'
#         k = '1'
#     elif int(k)==7:
#         try:
#             if int(l[i+1])>=4:
#                 r += '7'
#                 k = ''
#             else:
#                 r +='4'
#                 k = '1'
#         except:
#             r+='7'
#     elif int(k)>4:
#         r += '4'
#         k = '1'
#     elif int(k)==4:
#         try:
#             if int(l[i+1])>=4:
#                 r += '4'
#                 k = ''
#             else:
#                 k = '1'
#         except:
#             r+='4'
# print(int(r))

# 5회차_고해림:
# # 영화 감독 숌

# N = int(input())
# a = '666'
# number = 1
# count = 0

# while True:
#     if a in str(number):
#         count += 1
    
#     if count == N:
#         print(number)
#         break
    
#     number +=1