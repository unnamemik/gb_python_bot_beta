#t.me/gb_python_bot

import telebot
from telebot import types
import time
from telebot.apihelper import ApiTelegramException

token = "--------------------------------------------------------------------"
bot = telebot.TeleBot(token)
new_chat_id = '----------------'
frw_id = '----------------------'

global test_num
global true_answer
true_answer = 0

quest_text = ["  Ключевые слова в Python пишутся ...", "  Что выведет код? \nprint(type(1 / 2))",
              "  Выбери эквивалент random.randint(3, 6)", " Что выведет код? \nprint ((0 < 5 <= 3) and (0 / 0))",
              " Что делает функция open('file.txt', 'r+')?", " Чем являются функции в Python?",
              " Какая инструкция служит для создания анонимной функции?",
              " Что выведет код? \na = 'ab'\nb = 'bc'\nprint ('%sa, b' % a, b)",
              " Какая инструкция создает класс?", " Методы класса содержатся в пространстве имен..."]

answ = [["в нижнем регистре", "Ничего из перечисленного", "В ВЕРХНЕМ РЕГИСТРЕ", "С заглавной буквы"],
        ["type 'double' ", "type 'int' ", "type 'tuple' ", "type 'float'"],
        ["random.choice([3, 6]) ", "random.randrange(3, 6) ", "3 + random.randrange(3)", "3 + random.randrange(4)"],
        ["True", "False", "синтаксическая ошибка", "ZeroDivisionError"],
        ["Создание и редактирование файла", "Редактирование файла", "Чтение и редактирование файла", "Удаление файла"],
        ["Методами", "Экземплярами", "Классами", "Объектами"],
        ["omega", "anonymous", "lambda func", "lambda"],
        ["('ab', 'bc')a, b", "aba, b bc", "(ab, bc)a, c", "aba b, bc"],
        ["def Class", "Class class", "Нет верного ответа", "lambda class"],
        ["Класса", "Класса и экземплярах класса", "В экземплярах класса", "В глобальном пространстве имен"]]

answ_list = [" "," "," "," "," "," "," "," "," "," "]


@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
    # global new_chat_id
    # new_chat_id = message.chat.id
    global markup
    print(message.chat.id)
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    try:
        bot.send_message(message.chat.id, (
            f"\tПривет, @{user_name}! Добро пожаловать в наш серпентариум!\n\n\t"
            f"Цензуры у нас нет, зато есть несправедливый банхаммер для самых неспокойных."))
    except ApiTelegramException as e:
        if e.description == "Forbidden: bot was blocked by the user":
            print("2. Attention please! The user {} has blocked the bot.".format(user_name))
    try:
        bot.send_message(frw_id, f"Новый пользователь в чате: @{user_name} {user_id}")
    except ApiTelegramException as e:
        if e.description == "Forbidden: bot was blocked by the user":
            print("3. Attention please! The user {} has blocked the bot.".format(user_name))
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("А ты точно питонист?", url='t.me/gb_python_bot')
        markup.add(button1)
    try:
        bot.send_message(message.chat.id, "А теперь проверим, как ты умеешь шшшшипеть. "
                                          "\nИмей ввиду, мы тебя видим - откосить не получится. У тебя осталось не очень много времени, чтобы пройти тест. )".format(
            message.from_user), reply_markup=markup)
    except ApiTelegramException as e:
        if e.description == "Forbidden: bot was blocked by the user":
            print("4. Attention please! The user {} has blocked the bot.".format(user_name))


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        user_name = message.from_user.first_name
        user_id = message.from_user.id
        try:
            bot.send_message(frw_id, f"Пользователь @{user_name} {user_id} начал тест.")
        except ApiTelegramException as e:
            if e.description == "Forbidden: bot was blocked by the user":
                print("10. Attention please! The user {} has blocked the bot.".format(user_name))
        print(f"Пользователь @{user_name} {user_id} начал тест.")

        global true_answer
        true_answer = 0
        chat_id = message.chat.id
        try:
            bot.send_message(chat_id,
                             "Вопросов всего будет 10, они совсем не сложные. \n На каждый вопрос - 60 секунд, ответить надо на все.\n \n "
                             "Не торопись тыкать кнопки раньше времени - дождись следующего вопроса.")
        except ApiTelegramException as e:
            if e.description == "Forbidden: bot was blocked by the user":
                print("2. Attention please! The user {} has blocked the bot.".format(user_name))

        time.sleep(5)
        try:
            bot.send_message(chat_id, "Три...")
        except ApiTelegramException as e:
            if e.description == "Forbidden: bot was blocked by the user":
                print("2. Attention please! The user {} has blocked the bot.".format(user_name))
        time.sleep(0.5)

        try:
            bot.send_message(chat_id, "Два...")
        except ApiTelegramException as e:
            if e.description == "Forbidden: bot was blocked by the user":
                print("2. Attention please! The user {} has blocked the bot.".format(user_name))
        time.sleep(0.5)

        try:
            bot.send_message(chat_id, "Один...")
        except ApiTelegramException as e:
            if e.description == "Forbidden: bot was blocked by the user":
                print("2. Attention please! The user {} has blocked the bot.".format(user_name))
        time.sleep(0.5)

        try:
            bot.send_message(chat_id, "Поехали!!!")
        except ApiTelegramException as e:
            if e.description == "Forbidden: bot was blocked by the user":
                print("2. Attention please! The user {} has blocked the bot.".format(user_name))
            time.sleep(0.5)
        global test_num
        test_num = 0
        while test_num < 10:
            test(chat_id)
            time.sleep(60)

        if true_answer == 10 and test_num == 9:
            try:
                bot.send_message(chat_id, "Вау!!! Ты настолько крут, что заслуживаешь бонусного вопроса!")
            except ApiTelegramException as e:
                if e.description == "Forbidden: bot was blocked by the user":
                    print("4. Attention please! The user {} has blocked the bot.".format(user_name))
                time.sleep(3)
            try:
                bot.send_message(chat_id,
                                 "Файл foo.py содержит следующий код: \nclass Foo(object): \n\t\tdef __init__ (self, x): "
                                 "elf.val=x \n\t\tdef __str__ (self): return str(self.val)  \n\nСкрипт a.py содержит следующий код: \nimport pickle, foo, os"
                                 "\no = foo.Foo(list(range(4))) with open('temp.pkl', 'wb') as f: \n\t\tpickle.dump(o, f, pickle.HIGHEST_PROTOCOL) \nf.close() "
                                 "\n\nСкрипт b.py содержит следующий код: \nimport pickle with open('temp.pkl', 'r') as f: \n\t\tx = pickle.load(f) \nprint (x)"
                                 "\n\nУкажи результат последовательного выполнения скриптов a.py и b.py:")
            except ApiTelegramException as e:
                if e.description == "Forbidden: bot was blocked by the user":
                    print("5. Attention please! The user {} has blocked the bot.".format(user_name))
                time.sleep(10)
            try:
                bot.send_message(chat_id, "Ладно, это была шутка. \nВ следующий раз, а сейчас...))) ")
            except ApiTelegramException as e:
                if e.description == "Forbidden: bot was blocked by the user":
                    print("6. Attention please! The user {} has blocked the bot.".format(user_name))
            time.sleep(3)
            try:
                bot.send_message(chat_id, "Поздравляем! Ты достойная змеюка!")
            except ApiTelegramException as e:
                if e.description == "Forbidden: bot was blocked by the user":
                    print("7. Attention please! The user {} has blocked the bot.".format(user_name))
            bot.unban_chat_member(new_chat_id, user_id)
            markup_chat = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Добро пожаловать!", url='----------------------------')
            markup_chat.add(button1)
            try:
                bot.send_message(frw_id, f"Пользователь @{user_name} {user_id} прошел тест!",
                                 reply_markup=markup_chat)
            except ApiTelegramException as e:
                if e.description == "Forbidden: bot was blocked by the user":
                    print("8. Attention please! The user {} has blocked the bot.".format(user_name))
            print(f"Пользователь @{user_name} {user_id} прошел тест!")

        else:
            try:
                bot.send_message(chat_id, "Ты не прошел тест! Давай заново!")
            except ApiTelegramException as e:
                if e.description == "Forbidden: bot was blocked by the user":
                    print("9. Attention please! The user {} has blocked the bot.".format(user_name))
            try:
                bot.send_message(frw_id,
                                 f"Пользователь @{user_name} {user_id} не прошел тест, ответил на {true_answer} вопросов из 10.")
            except ApiTelegramException as e:
                if e.description == "Forbidden: bot was blocked by the user":
                    print("10. Attention please! The user {} has blocked the bot.".format(user_name))
            try:
                bot.ban_chat_member(new_chat_id, user_id)
            except ApiTelegramException as e:
                if e.description == "Forbidden: bot was kicked from the supergroup chat":
                    print("10. Attention please! The user {} has blocked the bot.".format(user_name))
                print(f"Пользователь @{user_name} {user_id} не прошел тест, ответил на {true_answer} вопросов из 10.")
    else:
        markup1 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Тык", url='t.me/gb_python_bot')
        markup1.add(button1)
        try:
            bot.send_message(message.chat.id, "Ходи сюда".format(message.from_user), reply_markup=markup1)
        except ApiTelegramException as e:
            if e.description == "Forbidden: bot was kicked from the supergroup chat":
                print("10. Attention please! The user has blocked the bot.")


def test(chat_id):
    murkup2 = types.InlineKeyboardMarkup(row_width=1, )
    but1 = types.InlineKeyboardButton(("A: " + answ[test_num][0]), callback_data='1')
    but2 = types.InlineKeyboardButton(("B: " + answ[test_num][1]), callback_data='2')
    but3 = types.InlineKeyboardButton(("C: " + answ[test_num][2]), callback_data='3')
    but4 = types.InlineKeyboardButton(("D: " + answ[test_num][3]), callback_data='4')
    murkup2.add(but1, but2, but3, but4)
    try:
        bot.send_message(chat_id, "Вопрос №" + str(test_num + 1) + quest_text[test_num], reply_markup=murkup2)
    except ApiTelegramException as e:
        if e.description == "Forbidden: bot was blocked by the user":
            print("12. Attention please! The user has blocked the bot.")


@bot.callback_query_handler(func=lambda call: True)
def answer(call: telebot.types.CallbackQuery):
    global test_num
    global true_answer
    print(test_num)

    if call.data == "1":
        bot.send_message(call.from_user.id, "A: " + answ[test_num][0])
        if answ[test_num][0] == answ_list[test_num]:
            true_answer = true_answer + 1
    elif call.data == '2':
        bot.send_message(call.from_user.id, "B: " + answ[test_num][1])
        if answ[test_num][1] == answ_list[test_num]:
            true_answer = true_answer + 1
    elif call.data == '3':
        bot.send_message(call.from_user.id, "C: " + answ[test_num][2])
        if answ[test_num][2] == answ_list[test_num]:
            true_answer = true_answer + 1
    elif call.data == '4':
        bot.send_message(call.from_user.id, "D: " + answ[test_num][3])
        if answ[test_num][3] == answ_list[test_num]:
            true_answer = true_answer + 1
    test_num += 1
    bot.answer_callback_query(callback_query_id=call.id)


try:
    bot.polling(none_stop=True, interval=0)
except ApiTelegramException as e:
    if e.description == "Forbidden: bot was blocked by the user":
        print("Connection closed")
