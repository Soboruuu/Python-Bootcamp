import weather
import sms
import stock


rain = weather.OpenWeatherMap()
market = stock.Stock()
message = f'Rain:\n{rain.call()}\n\nStock:\n{market.get_price()}'

send = sms.Twilio(message)

