# API
# application programming interface
# 컴퓨터나 컴퓨터 프로그램 사이의 연결
# 어플리케이션을 위한 인터페이스 (접면)

# 사용설명서
# api를 사용하기 전에 확인해야 할 것?
# 어떻게 조작하는지

# 주소를 통해서 요청을 보낸다
# 그렇게 보는 한 장의 문서

# 이미 받은 문서는 내 안에서 조작이 가능하다.

# 요청을 주소로 보내면 응답을 문서로 준다

# Hyper Text Transfer Protocol
# 주소로 요청을 주면 어떤 것을 준다.

# 빗썸 api
# http:// 
# 크롬이라는 브라우저에서 요청을 보내는 것
# python으로 요청을 보내고 싶다.

# request, python의 공식문서
# data.get('data').get(')

# 브라우저롤 통해 주소로 요청을 보내고 응답 결과를 브라우저가 웹 화면으로 랜더링 한다.
# 파이썬을 통해 주소로 요청을 보내고, 응답 결과를 파이썬으로 조작한다.

# API 활용 문서 예시
# 요청변수이름이 query, 값이 카카오 request response

# import requests

# students = ['gunhee', 'mingi', 'hyunyoung', 'minji', 'yuyoung']

# for name in students:
#     URL = f'https://api.nationalize.io/?name={name}'
#     response = requests.get(URL).json()
#     # print(response)
#     # print(response.get('country'))
#     # print(response.get('country')[0])
#     print(response.get('country')[0].get('country_id'))

# TMDB API 활용

import requests

# 
# 

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key' : '918218593bef22431edacf81eaab6317',
    'language' : 'ko-KR',
    'region' : 'KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)
print(response.get('results')[0])

# 백점이 맞는 게 아니라 성장이 맞는 거다
# 설명을 한 줄로 할 수 있으면 됐다. 그럼 됐다.
# 리스트와 소개팅 알아가는 과정

# 동료들을 

# 함께자라기 야생학습

# 복습위주, 알고리즘

# 작성을 디스코드에 피드백받기