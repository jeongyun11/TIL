import sys
sys.stdin = open('test.txt','r')
# 백준 2846번 오르막길
# input 받기 횟수n, 높이lng
n = int(input())
lng = list(map(int,input().split()))
# # print(lng,type(lng))
# 오르막길이 저장할 list 생성
li=[[] for i in range(n)]
j=0

# index error 때문에 만든 try except 구문.
# 오르막 값이면 li에 해당 오르막값 저장
for i in range(n):
    try:
        if lng[i]<lng[i+1]:
            li[j].append(lng[i])
            li[j].append(lng[i+1])
        else:
            j+=1
    except:
        pass
print(li)
# 오르막길이가 길면 이전 시행의 i+1과 다음 시행의 i가 값이 같아서, set으로 삭제
for _ in range(n):
    li[_]=list(set(li[_]))
print(li)
# 이중리스트로 저장되는데, 그 때 초기값과 맨 마지막 값 저장. 여기서도 역시 index
# error 때문에 try except 사용
for __ in range(n):
    try:
        # # print(li[__][0])
        li[__]=abs(li[__][0]-li[__][-1])
    except:
        pass
print(li)   
# for ind in range(n):
#     li.remove()
# li.replace('[]',0)

# 이중 리스트로 만들었는데, 원소가 list 타입일 때는 max 함수가 사용 불가하므로
# li2를 생성하여 빈 list 아닌 것만 추가
li2=[]
for ind in range(n):
    if li[ind]!=[]:
        li2.append(li[ind])
    # print(li2)
# max 사용하여 출력, li가 모두 빈 list였다면 출력 불가하므로 그 땐 0 출력
try:
    print(max(li2))
except:
    print(0)