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