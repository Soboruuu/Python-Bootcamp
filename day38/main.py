import datetime
import requests

# (0) 오늘 날짜/시간 구하고 포매팅하기
today = datetime.datetime.now().strftime("%Y/%m/%d")
now = datetime.datetime.now().strftime("%X")

# (1) nutritionix 로 운동 데이터를 구하기 위한 개인 신체 정보
age = int(input("How old are you?\n"))
gender = input("What is your sex? male/female\n")
weight_kg= int(input("What is your weight in kg?\n"))
height_cm=int(input("How tall are you in cm?\n"))
exercise_query = input("Which exercise did you do today?\n")

# (2) nutritionix 인증 정보, 분석할 운동 데이터
APP_ID = "Your App ID"
API_KEY = "Your Api Key"
nutritionix_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
nutritionix_body = {
    "query":exercise_query,
    "gender":gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

# (3) nutritionix에 운동 데이터 넘기고 json 파일로 분석 파일 받아오기
response = requests.post(url=nutritionix_endpoint, headers=nutritionix_headers, json=nutritionix_body)
response.raise_for_status()
result = response.json()
print(result)

# (4) sheety 인증 정보 및 nutritionix로 가져온 운동 분석 데이터(구글 시트에 넣어줄 데이터)
sheety_endpoint= "YOUR SHEETY ENDPOINT"

for exercise in result["exercises"]:
    sheety_inputs = {
        "시트1": {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# (4-1) Sheety API로 구글 시트에 운동 데이터 업로드하기 - Basic Authentication을 사용할 경우
sheety_response = requests.post(
  sheety_endpoint,
  json=sheety_inputs,
  auth=(
      "YOUR USERNAME",
      "YOUR PASSWORD",
  )
)

# (4-2) Sheety API로 구글 시트에 운동 데이터 업로드하기 - Bearer Token Authentication을 사용할 경우
bearer_headers = {
"Authorization": "Bearer YOUR TOKEN"
}
sheety_response = requests.post(
    sheety_endpoint,
    json=sheety_inputs,
    headers=bearer_headers
)
