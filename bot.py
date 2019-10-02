import pyowm
import telebot

owm = pyowm.OWM('9571c83a852b5fc9a8e2d5235e36eb2c', language = "ru")
bot = telebot.TeleBot("803669330:AAHhWsfqru8yUcDthHt_ZtiwctLDU0qwXxI")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура сейчас в районе " + str(temp) + "\n\n"

	if temp < 10:
		answer += "Сейчас пздц как холодно, одевай подштаники"
	elif temp < 20:
		answer += "Сейчас прохладно, но можно гулять"
	else:
		answer += "Температура норм"

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = False )
