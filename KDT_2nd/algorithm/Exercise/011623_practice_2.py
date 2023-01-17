# 10039
sum_score = 0

for i in range(5):
    score = int(input())
    if score < 40 :
        score = 40
    sum_score += score

print(int(sum_score / 5))


# 10871
n, x = map(int,input().split())
numbers = map(int,input().split())

for number in numbers :
    if number < x :
        print(number, end=' ')


# 2480
nums = list(map(int,input().split()))
a = nums[0]
b = nums[1]
c = nums[2]

if a == b == c :
    price = 10000 + a * 1000
elif a == b or a == c :
    price = 1000 + a * 100
elif b == c :
    price = 1000 + b * 100
else :
    price =max(nums) * 100

print(price)


# 10886
N = int(input())
cnt = 0
for n in range(N) :
    isCute = bool(input())
    cnt += isCute
if (N / 2) < cnt :
    print('Junhee is cute!')
else :
    print('Junhee is not cute!')


# 2506
N = int(input())
numbers = map(int, input().split())
cnt = 0
score = 0
for number in numbers : 
    if number == 1 :
        cnt += 1
    else :
        cnt = 0
        
    score += cnt

print(score)