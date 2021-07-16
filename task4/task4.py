import telebot
import requests
import json

Countries = ['USA', 'UKR', 'CAN', 'JPN', 'ITA']

def getData(iso):

    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/covid-ovid-data/sixmonth/"

    headers = {
        'x-rapidapi-key': "200109f47bmshe91f43046a9d637p115ecdjsne666b4a7da88",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url+iso, headers=headers)
    parsed = json.loads(response.text)
    return parsed

def getStat(array):
	statistics = []
	for item in array:
		res = getData(item)[0]
		statistics.append({
				"ISO" : res['symbol'],
				"Country" : res['Country'],
				"total_cases": res['total_cases'],
				"date" : res['date']
			})
	return statistics

bot = telebot.TeleBot('1827670136:AAHCEqPbp3-np2_3vuyfIXlUf3Hj6yEYyjY')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "/start":
      for item in getStat(Countries):
      	tmp = list(item.values())
      	print(" ".join(str(x) for x in tmp))
      	bot.send_message(message.from_user.id, " ".join(str(x) for x in tmp))

  else:
      bot.send_message(message.from_user.id, "I don't understand :(")

bot.polling(none_stop=True, interval=0)