# 노트 작성
# 작은 단계부터 점점 큰 단계로
# 메서드 없이 하고 그 다음 메서드를 사용
# print디버깅 습관화
# 이 악물고 이상해도 풀고 리팩토링을 고민하자
# solve AC정올 코드업 파이썬기초100제
word = 'starats'
start = 0
end = len(word) - 1
tnf = True
while start < end :
    if word[start] != word[end] :
        tnf = False
        break
    start += 1
    end -= 1
print(tnf)

# 리스트와 딕셔너리 특징과 시간 복잡도를 비교

# ----------------------------

# 딕셔너리

# 해시테이블?

# sha 256

# 인덱스 접근

# 존 요소를 찾으면
# 파이썬 딕셔너리

# 딕셔너리 O(1)
# 자료 탐색할 때
# 조회 dic[key],,,, dict.get(key, default)

# 딕셔너리 메서드
# 블라블라...
# 메서드와 내장함수

# 연습문제

# 단어를 기준으로 값을 찾는다 -> key value

# member[key].get(key,0) + 1

# from collections import Counter # 코테에서도 가능하다.

# 딕셔너리에서는 순서가 의미있나? 딕셔너리를 선택하는 기준은 순서가 아니라  값을 통해서 무언가를 판단하는 것은 딕셔너리
