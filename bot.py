import config
import telebot


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/bunny.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	bot.send_message(message.chat.id, "Welcome on board, {0.first_name}!\nI'm - {1.first_name}, <b>chat bot</b>.".format(message.from_user, bot.get_me()), parse_mode="HTML")

@bot.message_handler(content_types=['text'])
def blablabla(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
