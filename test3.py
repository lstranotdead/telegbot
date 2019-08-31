import pyowm
import telebot

owm = pyowm.OWM('f676c9b01bc8a23a44e47dbc1a00ebc5', language="ru")
bot = telebot.TeleBot("654970433:AAHN3QqZcRekJz4lSyl0JWRnSV6Sj8me0EA")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = " В місті " + message.text + " зараз " + w.get_detailed_status() + "\n\n"
    answer += " Температура зараз в районі " + str(temp) + "\n\n"

    if temp < 10:
    	answer += " Зараз дуже холодно, тепліше вдівайся "
    elif temp < 20:
    	answer += " На вулиці прохладно, вдівай курту "
    else:
    	answer += " Температура классна, вдівай що забажаєш "
    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )