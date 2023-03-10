import requests
from flight_data import FlightData

TEQUILA_URL = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = YOUR TEQUILA API KEY

ORIGIN_CITY = "LON" # <- 출발 도시 / 런던. 서울로 바꾸려면 "SEL"로

class FlightSearch:
    def get_iata_code(self, city_name):
        query={"term":city_name, "location_types":"city"}
        headers = {"apikey":TEQUILA_API_KEY}
        response = requests.get(url=f"{TEQUILA_URL}/locations/query",
        headers=headers, params=query)
        print(response.json())
        code = response.json()['locations'][0]['code']
        return code

    def search_flight(self,  destination_city_code, tomorrow, six_months):
        headers = {"apikey": TEQUILA_API_KEY}
        parameters = {
            "fly_from": ORIGIN_CITY,
            "fly_to": destination_city_code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"  # <- 통화. 미국 달러는 "USD", 한국 원은 "KRW"로 바꿀 수 있음
        }
        response = requests.get(url=f"{TEQUILA_URL}/v2/search", headers=headers, params=parameters)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
