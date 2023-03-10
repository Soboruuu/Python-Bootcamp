import requests
import datetime

# datetime 모듈 .strftime() 메소드로 YYYYMMDD 형태의 오늘 날짜 구하기
today = datetime.datetime.now().strftime("%Y%m%d")

# pixela 기본 정보
pixela_endpoint="https://pixe.la/v1/users"
pixela_username="yourusername"
pixela_token="yourapikey"
pixela_headers={"X-USER-TOKEN":pixela_token}
pixela_param = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# 1. pixela 계정 생성
response = requests.post(url=pixela_endpoint, json=pixela_param)

# 2. pixela 그래프 생성 (코딩 스터디, 시간, 소수점, 보라색)
pixela_graph_endpoint=f"{pixela_endpoint}/{pixela_username}/graphs"
pixela_graph_id="graph1"
graphs_config={
    "id": pixela_graph_id,
    "name": "Coding Study",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}
response=requests.post(url=pixela_graph_endpoint, headers=pixela_headers, json=graphs_config)

# 3. pixel 그래프 픽셀 데이터 생성 (오늘 날짜, 1.5시간 공부)
pixela_graph_post=f"{pixela_endpoint}/{pixela_username}/graphs/{pixela_graph_id}"
pixel_post={"date":today,
             "quantity": "1.5"}
response=requests.post(url=pixela_graph_post, headers=pixela_headers, json=pixel_post)

# 4. pixel 그래프 픽셀 데이터 수정 (오늘 날짜, 3.5시간 공부)
pixela_graph_update=f"{pixela_endpoint}/{pixela_username}/graphs/{pixela_graph_id}/{today}"
updated_pixel={"quantity": "3.5"}
# response = requests.put(url=pixela_graph_update, headers=pixela_headers, json=updated_pixel)

# 5. pixel 그래프 삭제
response = requests.delete(url=pixela_graph_update, headers=pixela_headers)
