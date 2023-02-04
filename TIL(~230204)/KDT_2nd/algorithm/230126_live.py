# 데이터 구조
# 데이터를 저장 다양하게 조작, 활용(crud)

# 문제를 더 효율적으로 풀기 위한 도구가 된다.

# 딕셔너리가 해쉬

# 순서가 아닌 형태로 접근

# 스택은 후입선출 오래된 늠은 썩고 새놈은 바로 사용
# 리스트 팝 어펜드 list[-1] top # 뒤로가기

# 괄호매칭

# 왼쪽괄호 입력수 
n = int(input())
a_list = list(range(1,n + 1))
a2_list = []
while True :
    a2_list.append(a_list.pop(0))
    if len(a_list) == 0 :
        break
    a_list.append(a_list.pop(0))

print(*a2_list)