import sys
sys.stdin = open('test.txt', 'r')
from pprint import pprint
from collections import deque
T = 10
for t in range(T) :
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    cnt_4 = 0

    nothing = input()
    test = list(input())
    print(f'#{t+1} ', end='')
    for i in test :
        
        if '{' == i : cnt_1 += 1
        elif '}' == i : cnt_1 -= 1
        elif '[' == i : cnt_2 += 1
        elif ']' == i : cnt_2 -= 1
        elif '(' == i : cnt_3 += 1
        elif ')' == i : cnt_3 -= 1
        elif '<' == i : cnt_4 += 1
        elif '>' == i : cnt_4 -= 1
        if cnt_1 < 0 :
            print(0)
            break
        elif cnt_2 < 0 :
            print(0)
            break
        elif cnt_3 < 0 :
            print(0)
            break
        elif cnt_4 < 0 :
            print(0)
            break
        # for j in [cnt_1, cnt_2, cnt_3, cnt_4] :
        #     if j < 0 : 
        #         print(0)
        #         break

    else : print(1)