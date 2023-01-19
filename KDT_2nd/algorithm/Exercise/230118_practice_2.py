# 9498
score = int(input())

if score >= 90 :
    print('A')
elif score >= 80 :
    print('B')
elif score >= 70 :
    print('C')
elif score >= 60 :
    print('D')
else :
    print('F')


# 9093
T = int(input())

for t in range(T) :
    string_str = input()
    string_list = string_str.split()

    for word in string_list : 
        print(word[::-1], end=' ')

    print()


# 11721
word = input()
length = 0

while True :

    length += 10


    if length >= len(word) :
        print(word[length -10 : len(word)])
        break
    
    print(word[length -10 : length])


# 2947
numbers = list(map(int,input().split()))
while True :
    for i in range(len(numbers) - 1) :
        if numbers[i] > numbers[i + 1] :
            temp = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = temp
            print(*numbers)
    if numbers == sorted(numbers) :
        break
