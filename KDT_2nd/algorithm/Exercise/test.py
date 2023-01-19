import sys
sys.stdin = open("test.txt","r")

N = int(input())
numbers = list(map(int, input().split()))

number_max = max(numbers)


for number in numbers :
    # if number != number_max :
    number = number / number_max * 100
print(numbers)
print(sum(numbers)/N)