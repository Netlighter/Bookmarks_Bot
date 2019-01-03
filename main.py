import telebot
from telebot import apihelper
from telebot import types


import settings


apihelper.proxy = {'https':settings.PROXY}

bot = telebot.TeleBot(settings.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(
        message.from_user.id,
        '''*This is a simple Bookmarks bot.*

        _Let\'s start using!_
        Just simply send any type of file (including text) and I\'ll save it to your personal bookmarks, that you can use wherever you are.''',
        parse_mode = 'Markdown')

    @bot.message_handler(commands=['git'])
    def send_git(message):
        bot.send_message(
        message.from_user.id,
        '[My git REPO](https://github.com/Netlighter/Bookmarks_Bot)',
        parse_mode = 'Markdown')


    @bot.message_handler(content_types=[
    'text',
    'photo',
    'document',
    'audio',
    'voice',
    'video_note',])
    def add_bookmark(message):
        #broken code...

        if message.content == 'text'

        bot.send_photo(message.from_user.id, message.photo[-1].file_id)


bot.polling()
