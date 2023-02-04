# 2789
word = input()
result = ''
for w in word :
    if w not in 'CAMBRIDGE' :
        result += w
print(result)


# 2675
T = int(input())

for t in range(T) :
    R,S = input().split()
    R = int(R)

    for s in S :
        print(s*R, end='')
    print()


# 10988
word = input()
if word == word[::-1] :
    print(1)
else :
    print(0)


# 17249
taebo = input()
# cnt = 0
# for i in taebo :
#     if i == '@' :
#         cnt +=1
#     elif i == '0' :
#         print(cnt,end = ' ')
#         cnt = 0
# print(cnt)

# 인덱스로 위치받고 슬라이스로 카운트
mouse = taebo.index('0')
print(taebo[:mouse].count('@'), taebo[mouse:].count('@'))


# 2941
croatia = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in croatia :
    if i in word :
        word = word.replace(i,'.')
print(len(word))


# 10809
word = input()

for i in range(97,123) :
    if chr(i) in word :
        print(word.find(chr(i)), end=' ')
    else :
        print(-1, end=' ')

