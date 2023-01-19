# 9085
T = int(input())

for t in range(T) : 
    N = int(input())
    print(sum(map(int, input().split())))


# 10824
numbers = list(input().split())

print(int(numbers[0] + numbers[1]) + int(numbers[2] + numbers[3]))


# 3009
set_x = set()
set_y = set()
list_xy = []
for i in range(3) :
    x,y = map(int,input().split())
    list_xy.append([x,y])
    set_x.add(x)
    set_y.add(y)

for x in set_x :
    for y in set_y :
        if [x, y] not in list_xy :
            print(*[x, y])
            break

# 블로그 컨닝
list_x = []
list_y = []

for i in range(3) : 
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

for i in range(3) :
    if list_x.count(list_x[i]) == 1 : 
        x = list_x[i]
    if list_y.count(list_y[i]) == 1 : 
        y = list_y[i]
print(x, y)


# 10952
while True :
    a, b = map(int,input().split())

    if (a == 0) and (b == 0) :
        break

    print(a + b)
    # tnf = a and b # 같아야 트루가 반환


# 1110
num_str = input()
if int(num_str) < 10 :
    num_str += '0'
num_first = num_str
count = 0

while True :
    sum_one = 0
    for num_one in num_str :
        sum_one += int(num_one)

    num_str = num_str[-1] + str(sum_one)[-1]
    count += 1

    if num_str == num_first :
        break

print(count)

# 블로그 참조
num = int(input())
num_first = num
count = 0

while True :
    num_tenth = (num // 10) + (num % 10)
    if num_tenth >= 10 : 
        num_tenth -= 10
        
    num = num_tenth + (num % 10) * 10
    
    count += 1
    if num == num_first :
        break

print(count)
