# 9012.
T = int(input())
for t in range(T) :
    PS_str = input()
    PS_list = []
    result = 'YES'

    for ps in PS_str :
        if ps == '(' :
            PS_list.append(ps)
        else : # ')'
            if PS_list :
                PS_list.pop()
            else :
                result = 'NO'
                break
    if PS_list :
        result = 'NO'

    print(result)

# 