# 1453. 해시
N = input()
numbers = map(int,input().split())
seat = set()
cnt = 0
for number in numbers :
    if number not in seat :
        seat.add(number)
    else : 
        cnt += 1
print(cnt)