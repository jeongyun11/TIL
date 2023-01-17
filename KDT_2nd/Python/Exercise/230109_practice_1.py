# 1.
a = int(input())
print(a)


# 2. 
a, b = map(int,input().split())
print(a,b)


# 3. 
numbers = list(map(int, input().split()))

for number in numbers :
    print(number, end = ' ')

print()


# 4. 
str = list(input().split())

for word in str :
    print(word, end = ' ')

print()


# 5. 
str = list(input().split())

for i,j in enumerate(str) :
    print(i, j)

for i, word in enumerate(str) : 
    str[i] = int(word)

for word in str : 
    print(word)
    print(type(word))


# 6. 
a, b = map(int, input().split())


# 7. 
list_Word = list(input().split())


# 8. 
list_Number = list(map(int,input().split()))


# 9.
list_Number = list(map(int,input().split()))