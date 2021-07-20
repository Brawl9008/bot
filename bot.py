import telebot
bot = telebot.TeleBot('1928828935:AAH2youCA7_qotbWPDB590LnFFK5ULFgEYg')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'приветсвую, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет! Бот еще в разработке.')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

bot.polling(none_stop=True)
