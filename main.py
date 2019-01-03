import telebot
from telebot import apihelper


import settings


apihelper.proxy = {'https':settings.PROXY}

bot = telebot.TeleBot(settings.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(
        message.from_user.id,
        '*This is a simple Bookmarks bot.*' +
        '\n\n' +
        '_Let\'s start using!_' +
        '\n' +
        'Just simply send any type of file (including text) and I save it to you personal bookmarks, which you can use anywhere you are.',
        parse_mode = 'Markdown')

    bot.send_photo(message.from_user.id, 'AgADAgADxakxG3J-cUmyIQrGeEoOrG5MOQ8ABD7pse51WVJeG0YBAAEC')
bot.polling()
