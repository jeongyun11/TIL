# 코드는 짧게 보다는 현명하게
# 파이썬은 1초에 1억번
# while은 종료 조건을 먼저 짠다

# 결과를 보고 원인을 본다.

# 내 호흡에 맞춰라

# 덩어리를 나누고 for과 if를 크게 묶고 하나씩 접근

# 깨봉수학, 칸아카데미

#선대는 mit 선대 무료로 유튜브에 올라와있어요 3blue 1

# 비선형 자료구조

# vertex : 정점, 노드, 간선으로 연결되는 객체 (동그라미)

# edge : 간선, 정점 간의 관계를 표현하는 선

# path : 경로, 시작정점 ~ 도착정점 정점기준으로나열

# adjacencu : 인접, 두개의 정점이 하나의 간선으로 직접 연결된 상태

# 무방향그래프
# 차수 : 하나의 정점에 연결된 간선의 수
# 모든 정점의 차수의 합 = 간선 수 * 2

# 유방향그래프
# 차수 : 진입차수와 진출차수로 나누어짐 
# - 외부정점에서 한 정점으로 들어오는 간선의수
# - 한 정점에서 외부 으로 나가는 간선의수

# 리스트로 담거나 행렬로 담거나 인접행렬 인접리스트
# X = 3
# Y = 4
# list1 = [[0 for x in range(X)] for y in range(Y)]
# list2 = [[0] * X for y in range(Y)]

# for y in range(Y) :
#     print(list1[y])

# print()

# for y in range(Y) :
#     print(list2[y])

# 정점이 많고 간선이 적으면 리스트
# 정점이 적으면 간선이 많고 행렬


# 정점이 많고 간선이 적은 리스트 -> 행렬
from pprint import pprint
index = 10

matrix1 = [[0* i for i in range(index)] for i in range(index)]

for v1, v2 in [(2, 6), (3, 0), (3, 1)] :
    matrix1[v1][v2] = 1
    matrix1[v2][v1] = 1

pprint(matrix1)
print()

list1 = [[] for i in range(index)] # 빈 리스트를 형성

# for y in range(Y) :
#     v1, v2 = map(int, input().split())
#     list1[v1].append(v2)
#     list1[v2].append(v1) # 
for v1, v2 in [(2, 6), (3, 0), (3, 1)] :
    list1[v1].append(v2)
    list1[v2].append(v1) # 

pprint(list1)
print()
# N = int(input())
# for i in range(N) :
#     v1, v2 = map(int, input().split())
#     matrix1[v1][v2] = 1
#     matrix1[v2][v1] = 1
# matrix1[2][6] = 1
# matrix1[6][2] = 1
# matrix1[3][0] = 1
# matrix1[0][3] = 1

# 튜플로
print('--------------------------')
print()
# 정점이 적고 간선이 많은 행렬 -> 리스트
index = 4
list2 = [[] for i in range(index)]

for v1, v2 in [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)] :
    list2[v1].append(v2)
    list2[v2].append(v1)

for i in range(index) :
    print(list2[i])
print()

matrix2 = [[0 for i in range(index)] for i in range(index)]

for v1, v2 in [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)] :
    matrix2[v1][v2] = 1
    matrix2[v2][v1] = 1

for i in range(index) :
    print(matrix2[i])
print()
# 정점이 N일 때 가지는 최대 간선 개수 : (N-1)! = N(N-1)/2