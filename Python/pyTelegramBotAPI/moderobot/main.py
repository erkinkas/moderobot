#!/usr/bin/python
import os
import telebot

API_TOKEN = os.environ["TELEBOT_BOT_TOKEN"]

text_messages = {
    'welcome':
        u'Please welcome {name}!\n\n'
        u'This chat is intended for questions about and discussion of the pyTelegramBotAPI.\n'
        u'To enable group members to answer your questions fast and accurately, please make sure to study the '
        u'project\'s documentation (https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md) and the '
        u'examples (https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples) first.\n\n'
        u'I hope you enjoy your stay here!',

    'info':
        u'My name is TeleBot,\n'
        u'I am a bot that assists these wonderful bot-creating people of this bot library group chat.\n'
        u'Also, I am still under development. Please improve my functionality by making a pull request! '
        u'Suggestions are also welcome, just drop them in this group chat!',

    'wrong_chat':
        u'Hi there!\nThanks for trying me out. However, this bot can only be used in the pyTelegramAPI group chat.\n'
        u'Join us!\n\n'
        u'https://telegram.me/joinchat/067e22c60035523fda8f6025ee87e30b'
}

bot = telebot.AsyncTeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    print('send_welcome')
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=["ping"])
def on_ping(message):
    print('on_ping')
    bot.reply_to(message, "Still alive and kicking!")


@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def on_user_joins(message):
    print('on_user_joins')
    new_chat_members = message.new_chat_members

    for new_member in new_chat_members:
        name = new_member.first_name
        if hasattr(new_member, 'last_name') and new_member.last_name is not None:
            name += u" {}".format(new_member.last_name)

        if hasattr(new_member, 'username') and new_member.username is not None:
            name += u" (@{})".format(new_member.username)

        bot.reply_to(message, text_messages['welcome'].format(name=name))


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print('echo_message')
    bot.reply_to(message, message.text)


def listener(messages):
    for m in messages:
        print(str(m))


print('started')
bot.set_update_listener(listener)
bot.polling()
