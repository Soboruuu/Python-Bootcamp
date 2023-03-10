from data_manager import DataManager
import flight_search
import datetime
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = flight_search.FlightSearch()
sheet_data = data_manager.get_data()
notification_manager = NotificationManager()

for item in sheet_data:
    if item['iataCode'] == "":
        item['iataCode'] = flight_search.get_iata_code(city_name=item['city'])
        data_manager.update_destination_code(sheet_data)
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    sixmonths = datetime.date.today() + datetime.timedelta(days = 180)
    flight = flight_search.search_flight(destination_city_code=item['iataCode'],tomorrow=tomorrow, six_months=sixmonths)
    if int(flight.price) < int(item["lowestPrice"]):
        notification_manager.send_sms(
            message=f"Low price alert! Only {flight.price} GBP to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )

users = data_manager.get_customer_emails()
emails = [row["email"] for row in users]
names = [row["firstName"] for row in users]

message = f"Low price alert! Only {flight.price}GBP to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
if flight.stop_overs > 0:
    message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

notification_manager.send_emails(emails, message)
