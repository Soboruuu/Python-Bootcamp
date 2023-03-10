import requests

SHEETY_URL = YOUR SHEETY URL

class DataManager:
    def __init__(self):
        self.data = {}

    def get_data(self):    
        response = requests.get(url=SHEETY_URL)
        response.raise_for_status()
        self.data = response.json()['prices']
        print(self.data)
        return self.data

    def update_destination_code(self, sheet_data):
        for row in sheet_data:
            new_data = {"price":{"iataCode": row["iataCode"]}}
            response = requests.put(url=f"{SHEETY_URL}/{row['id']}", json=new_data)
            print(response.text)
