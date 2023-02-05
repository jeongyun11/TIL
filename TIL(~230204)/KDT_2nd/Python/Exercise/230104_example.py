# 1. 
list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)

for element in list_variable[1:] : # slice는 0부터 시작한다.
    print(element)

'''
2
3
4
5
7
8
'''


# 2. 
for element in range(-2, 10, 2) :
    print(element, end=' ')
'''
-2 0 2 4 6 8
'''


# 3. 
a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n) :
    if number % 2 == 0 : 
        a = a + 1

    if number % 3 == 0 : 
        b = b + 1

    if number % 4 == 0 : 
        c = c + 1

    if number % 5 == 0 : 
        d = d + 1

print(a, b, c, d) # 5 4 3 2


# 4. 
i = 0
while i <= 10 : 
    print(i)
    i = i + 1

'''
0
1
2
3
...
9
10
'''


# 5.
i = 0
while i <= 10 : 
    i = i + 1
    print(i)
    
'''
1
2
3
...
9
10
11
'''


# 6. 
i = 0
while i <= 10 :
    i = i + 2
    print(i)

'''
2
4
6
8
10
12
'''


# 7. 
i = 0
while True :
    print(i)
    i = i + 1
    if i > 10:
        break

'''
0
1
...
9
10
'''
i = 0
while i <= 10 :
    print(i)
    i = i + 1

'''
0
1
...
10
'''


# 8. 오답 
i = 0
while True : 
    print(i)
    if i > 10 : 
        break
    i = i + 1

'''
0
1
2
...
11
'''


# 9. 
list_variable = list(range(0,7))
print(len(list_variable)) # 7


# 10.
list_variable = list(range(0,7))
print(sum(list_variable)) # 21


# 11.
list_variable = [3, 1, 4, -3, 9, 7]
print(min(list_variable) - max(list_variable)) # -12