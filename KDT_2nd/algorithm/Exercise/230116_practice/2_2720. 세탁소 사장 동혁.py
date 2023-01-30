# 2720. 
T = int(input())

for t in range(T) :
    money = int(input())
    calcul_list = []

    calcul_list.append(money // 25)
    money = money % 25

    calcul_list.append(money // 10)
    money = money % 10
    
    calcul_list.append(money // 5)
    money = money % 5

    calcul_list.append(money)

    print(*calcul_list)