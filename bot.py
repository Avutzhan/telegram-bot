import config
import telebot
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

# send welcome message and sticker
@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/bunny.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Random number")
	item2 = types.KeyboardButton("How are you?")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Welcome on board, {0.first_name}!\nI'm - {1.first_name}, "
									  "<b>chat bot</b>.".format(message.from_user, bot.get_me()),
					 				parse_mode="HTML", reply_markup=markup)

# echo method retuns entered string
@bot.message_handler(content_types=['text'])
def blablabla(message):
	if message.chat.type == 'private':
		if message.text == 'Random number':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == 'How are you?':

			# inline keyboard
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Good", callback_data='good')
			item2 = types.InlineKeyboardButton("Bad", callback_data='bad')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Fine and you?', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'i don`t know')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.message:
		if call.data == 'good':
			bot.send_message(call.message.chat.id, 'This is awesome')
		elif call.data == 'bad':
			bot.send_message(call.message.chat.id, 'Bivaet')

		# remove inline buttons
		bot.edit_message_text(chat_id=call.message.chat.id,
							  message_id=call.message.message_id,
							  text="How are you?",
							  reply_markup=None)
		# show alert
		bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
								  text="Test Alert")


bot.polling(none_stop=True)
