# import sys
# sys.stdin = open('test.txt', 'r')

# 1547.
M = int(input())
result = 1

for i in range(M) :
    cup_num = list(map(int,input().split()))

    for i in range(2) :
        if result == cup_num[i] :
            result = cup_num[1-i]
            break

print(result)


# 5576.
for i in range(2) :
    print(sum(sorted([int(input()) for i in range(10)], reverse=True)[:3]), end=' ')
print()


# 2846.
N = int(input())
he = list(map(int, input().split()))
start = he[0]
result = []

for i in range(1, N) :
    if he[i-1] < he[i] : 
        end = he[i]

        if (i == N-1) or (he[i] >= he[i+1]) :
            result.append(end - start)    

    else : 
        start = he[i]
if result :
    print(max(result))
else :
    print(0)


# 1251.
word = input()
word_list = []
for i in range(1, len(word)-1) :
    for j in range(i+1, len(word)) :
        word_list.append(word[i-1::-1]+word[j-1:i-1:-1]+word[:j-1:-1])
print(sorted(word_list)[0])

