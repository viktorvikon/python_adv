from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import mongoengine as me

TOKEN = '1324482133:AAFFNciJxhpEZD07PhlDoTQhODYbHCXEAKs'


DB_NAME = 'users'
information = {}

bot = TeleBot(TOKEN)
me.connect(DB_NAME)


class User(me.Document):

    name = me.StringField(required=True)
    phone = me.StringField(required=True)
    email = me.StringField(required=True)
    address = me.StringField(required=True)
    wishes = me.StringField(required=True)


@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Да', callback_data='yes')
    button2 = InlineKeyboardButton('Нет', callback_data='no')
    kb.add(button1, button2)

    bot.send_message(message.chat.id, 'Здравствуйте. Пройдите пожалуйста небольшой опрос. Согласны?',
                     reply_markup=kb
                     )


@bot.callback_query_handler(func=lambda call: call.data == 'no')
def bye(call):
    bot.send_message(call.from_user.id, 'До свидания')


@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def start(call):
    bot.send_message(
        call.from_user.id,
        'Здравствуйте! Какая Вас зовут?'
    )


@bot.message_handler(content_types=['text'])
def get_name(message):
    information['name'] = message.text
    bot.send_message(
        message.chat.id,
        'Какой у Вас номер телефона?'
    )
    bot.register_next_step_handler(message, get_phone)


@bot.message_handler()
def get_phone(message):
    information['phone'] = message.text
    bot.send_message(
        message.chat.id,
        'Какой у Вас e-mail?'
    )
    bot.register_next_step_handler(message, get_email)


def get_email(message):
    information['email'] = message.text
    bot.send_message(
        message.chat.id,
        'Какой Ваш адрес?'
    )
    bot.register_next_step_handler(message, get_address)


def get_address(message):
    information['address'] = message.text
    bot.send_message(
        message.chat.id,
        'Какие у Вас есть пожелания?'
    )
    bot.register_next_step_handler(message, get_wishes)


def get_wishes(message):
    information['wishes'] = message.text
    User.objects.create(**information)
    bot.send_message(message.chat.id, 'Спасибо.')


bot.polling()
