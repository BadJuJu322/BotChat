import time
import webbrowser
import datetime
import emoji
import telebot

allowed_usernames = ["MashaLalala3377400001999755599","isayzi", "JadBuBu", "nixxzq", "ImaoryI"]
bot = telebot.TeleBot('6846130267:AAGRNpl7damVs0f61p9uwXJm1XgZRknO0AQ')



@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    welcome_message = (
        "Приветствую вас в нашем чате! Пожалуйста, ознакомьтесь с правилами :\n"
        f"1. Никакой рекламы без согласования с администрацией.\n"
        f"2. Никакого 18+ контента, спама.\n"
        f"3. Разрешено писать только с одного аккаунта, твинки запрещены, каналы запрещены.\n"
        f"4. Неадекватное и оскорбительное поведение карается мутом на день, после трёх предупреждений выдаётся перманентный бан.\n"
        f"5. Все конфликты решаются в лс, не засоряйте чат и не впутывайте в это модерацию .\n"
        "\n"
        "Наш Discord канал - [Тык!](https://discord.gg/maory)\n"
        "Наш Minecraft сервер с модами - [Тык!](https://drive.google.com/file/d/1N4ZDeIH7fwuV13O6TdnilIHz-YFniJLk)\n"
        "Список доступных команд  :\n"
        "/servеr , /rulеs , /disсord "
    )

    bot.send_message(message.chat.id, welcome_message, parse_mode='Markdown')

@bot.message_handler(commands=['rules','правила','Правила','Rules'])
def rules(message):
    mess = '1. Никакой рекламы без согласования с администрацией.\n2. Никакого 18+ контента, спама.\n3. Разрешено писать только с одного аккаунта, твинки запрещены, каналы запрещены.\n4. Неадекватное и оскорбительное поведение карается мутом на день, после трёх предупреждений выдаётся перманентный бан.\n5. Все конфликты решаются в лс, не засоряйте чат и не впутывайте в это модерацию.\n p.s За спам казино,боулингом,баскетболом и подобным, мут (не больше раза в сутки >:)  )'
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['server','minecraft','сервер','майнкрафт','Server','Micenraft','Майнкрафт','Сервер'])
def server(message):
    link = "https://drive.google.com/file/d/1N4ZDeIH7fwuV13O6TdnilIHz-YFniJLk"
    text = f"Наш Minecraft сервер с модом на покемонов, ссылка на архив со всеми необходимыми файлами - [Тык!]({ link })"
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

@bot.message_handler(commands=['discord','Discord','дискорд','Дискорд'])
def discord(message):
    link = "https://discord.gg/maory"
    text = f"Мой Дискорд канал - [Тык!]({ link })"
    bot.send_message(message.chat.id, text, parse_mode='Markdown')


@bot.message_handler(commands=['kick','кик','3'])
def kick_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if message.from_user.username not in allowed_usernames:
            bot.reply_to(message, "Тебе нельзя, лапки не доросли :/ .")
            return
        if user_status == 'administrator' or user_status == 'creator' or message.from_user.username in allowed_usernames :
            bot.reply_to(message, 'Брат, не туда воюешь...' )
        else:
            bot.kick_chat_member(chat_id,user_id)
            bot.reply_to(message,f'Пользователь {message.reply_to_message.from_user.username} вылетел отсюда.')
    else:
        bot.reply_to(message,'Используй команду в ответ на сообщение')


@bot.message_handler(commands=['mute','мут','1'])
def mute_user(message):
    if message.reply_to_message:
        chat_id=message.chat.id
        user_id=message.reply_to_message.from_user.id
        user_status=bot.get_chat_member(chat_id,user_id).status
        if message.from_user.username not in allowed_usernames:
            bot.reply_to(message, "Куда лапы тянешь! >:(.")
            return
        if user_status == 'administrator' or user_status == 'creator' or message.from_user.username in allowed_usernames:
            bot.reply_to(message,'Брат, не туда воюешь...')
        else:
            duration = 60  # Значение по умолчанию - 1 минута
            args = message.text.split()[1:]
            if args:
                try:
                    duration = int(args[0])
                except ValueError:
                    bot.reply_to(message, "Неправильный формат времени.")
                    return
                if duration < 1:
                    bot.reply_to(message, "Время должно быть положительным числом.")
                    return
                if duration > 1440:
                    bot.reply_to(message, "Максимальное время - 1 день(1440).")
                    return
            bot.restrict_chat_member(chat_id, user_id, until_date=time.time() + duration * 60)
            bot.reply_to(message,f"Пользователь {message.reply_to_message.from_user.username} замьючен на {duration} минут.")

    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение дурашки, которого нада замутить.")

@bot.message_handler(commands=['unmute','размут', '2'])
def unmute_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        if message.from_user.username not in allowed_usernames:
            bot.reply_to(message, "Куда мы лезем! >:).")
            return
        bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
        bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} размьючен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого нада размутить.")


# Запуск бота
bot.polling(none_stop=True)
