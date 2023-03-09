import requests

api_endpoint = "https://opentdb.com/api.php"
parameter = {"amount": 10, "type": "boolean"}


response = requests.get(api_endpoint, params=parameter)
quiz_data = response.json()
print(quiz_data)

question_data = quiz_data['results']
print(question_data)
