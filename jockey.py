import telegram
import json
import requests
import time
import sys

bot=telegram.Bot(token='---YOUR TOKEN HERE---')
chat_id = bot.getUpdates()[-1].message.chat_id
#credits for random jokes : https://github.com/KiaFathi/tambalAPI 
joke_url ='http://tambal.azurewebsites.net/joke/random'

welcome = 'AHOY!\nJOCKEY is a simple joke telling bot, type \'stop\' whenever you wish to.'
bot.sendMessage(chat_id=chat_id, text=welcome)

def firstcall(x):
	if x == 1:
		bot.sendMessage(chat_id=chat_id, text="Bye, See you again!")
		sys.exit()	
	else:
		r = requests.get(joke_url)
		data = json.loads(r.text)
		bot.sendMessage(chat_id=chat_id, text=data['joke'])

while 1:
	updates = bot.getUpdates()
	commands = [u.message.text for u in updates]
	latestCommand = commands[-1]
	if latestCommand not in('stop', 'Stop', 'STOP'):
		firstcall(2)
	else :
		firstcall(1)
	time.sleep(3)