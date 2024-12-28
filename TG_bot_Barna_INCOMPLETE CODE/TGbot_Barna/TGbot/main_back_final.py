# FROM AND IMPORT DELETE
# FROM AND IMPORT DELETE
# FROM AND IMPORT DELETE
# FROM AND IMPORT DELETE

############ DONT START ################
TG IS A BOT. THE CODE IS INCOMPLETE. Some of the code has been deleted.  Copyright
TG БОТ. КОД НЕПОЛНЫЙ. Часть кода была удалена.  АВТОРСКОЕ ПРАВО
 DONT START


TG IS A BOT. THE CODE IS INCOMPLETE. Some of the code has been deleted.  Copyright
TG БОТ. КОД НЕПОЛНЫЙ. Часть кода была удалена.  АВТОРСКОЕ ПРАВО
TG IS A BOT. THE CODE IS INCOMPLETE. Some of the code has been deleted.  Copyright
TG БОТ. КОД НЕПОЛНЫЙ. Часть кода была удалена.  АВТОРСКОЕ ПРАВО
TG IS A BOT. THE CODE IS INCOMPLETE. Some of the code has been deleted.  Copyright
TG БОТ. КОД НЕПОЛНЫЙ. Часть кода была удалена.  АВТОРСКОЕ ПРАВО




tracemalloc.start()





bot = AsyncTeleBot(TOKEN)

# Словарь для хранения состояний пользователей
user_states = {}

async def send_mail(subject, to, msg):
    message = MIMEMultipart()
    message["From"] = EMAIL1
    message["To"] = to
    message["Subject"] = subject
    message.attach(MIMEText(msg, "html", "utf-8"))



    

    smtp_client = SMTP(hostname="smtp.mail.ru", port=465, use_tls=True)
    async with smtp_client:
        await smtp_client.login(EMAIL1, PWD1)
        await smtp_client.send_message(message)






dp = bot



products = [
    "Вода артезианская питьевая (19 л.)",
    "Вода артезианская питьевая (5 л.)",
]
def create_product_keyboard():
    """Создает инлайн-клавиатуру для выбора товара."""
    keyboard = types.InlineKeyboardMarkup()

@dp.message_handler(commands=['start'])
async def send_product_list(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказ питьевой воды")
    item2 = types.KeyboardButton("Инструкция по заказу")
    item3 = types.KeyboardButton("О нас")
    item4 = types.KeyboardButton("Узнать цены")


# @bot.message_handler(commands=['price'])
# async def price(message: types.Message):
#     await bot.send_message(message.chat.id, commands.price)
@bot.message_handler(commands=['button'])
async def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказ питьевой воды")
    item2 = types.KeyboardButton("Инструкция по заказу")
    item3 = types.KeyboardButton("О нас")
    item4 = types.KeyboardButton("Узнать цены")
    item5 = types.KeyboardButton("Наш номер телефона")
    item6 = types.KeyboardButton("Наш график доставки")
    markup.add(item1, item2, item3, item4, item5, item6)
    



@bot.message_handler(func=lambda message: message.text.lower() in commands.word_phone)
async def start_registration(message):
    await bot.send_message(message.chat.id, commands.phone)

@bot.message_handler(func=lambda message: message.text.lower() in commands.word_help1)
async def start_registration(message):
    await bot.send_message(message.chat.id, commands.help1)

@bot.message_handler(func=lambda message: message.text.lower() in ["start", "", "старт", "бот", "старт бота", "запуск", "запустить"])
async def start_registration(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Заказ питьевой воды")
    item2 = types.KeyboardButton("Инструкция по заказу")
    item3 = types.KeyboardButton("О нас")
    item4 = types.KeyboardButton("Узнать цены")

    markup.add(item1, item2, item3, item4, item5, item6)
    
    await bot.send_message(message.chat.id, commands.start, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() in ["узнать цены", "/price", "price", "прайс", "цены", "узнать цены"])
async def start_registration(message):
    await bot.send_message(message.chat.id, commands.price)













cities = [
    "Нижний Тагил",
    "Баранчинский",
    "Кушва, Верхняя Тура",
    "Красноуральск",


]
zakaz = [
    "Да",
    "Нет"

]
soglas = [
    "Согласен(а)",
    "Не согласен(а)"

]

def create_sogl_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    for sogl in soglas:


        # state['step'] += 1  # Переход на следующий шаг
        user_states[user_id] = state  # Сохраняем обновленное состояние
        if callback_query.data == "Согласен(а)":


        



            id = state['data']['id']
            name = state['data']['name']
            city = state['data']['city']
            number = state['data']['number']
            date = state['data']['date']
            counts = state['data']['counts']
            tovar = state['data']['tovar']
            prod = state['data']['prod']
            comm = state['data']['comm']
            keyboard = create_zakaz_keyboard()
            await bot.send_message(user_id, 
            f"""Ваш заказ:
Фамилия или название организации - {id}
Город доставки - {tovar}
Продукт - {prod}
Количество - {name}
Адрес доставки - {city}






def create_zakaz_keyboard():
    keyboard = types.InlyboardMarkup()
    for anketa in zakaz:
        button = types.I(text=anketa, callback_data=anketa)
        keyboard.add(button)
    return keyboard
@dp.ca_query_handler(lambda c: c.data in zakaz)
async def process_zakaz_selection(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    state = user_states.get(user_id)
    if callback_query.data ==  "Нет":
        del user_states[user_id]
        await bot.send_message(user_id, "Ваша заявка отменена")
        

    if ery.data == "Да":
        id = state['data']['id']
        name = state['data']['name']
        city = state['data']['city']
        number = state['data']['number']
        date = state['data']['date']
        counts = state['data']['counts']
        tovar = state['data']['tovar']
        prod = state['data']['prod']
        comm = state['data']['comm']

                    


        await bot.send_message(user_id, "Спасибо за Ваше сообщение. Мы свяжемся с Вами в ближайшее время!")
        await bot.send_message(user_id, 'Если вы хотите сделать ещё заказ, напишите /order или "заявка"')
        await send_mail('Заказ Воды ТЕЛЕГРАМ БОТ', EMAIL1, 
        f"""
            <strong>Фамилия или название организации - </strong>{id}<br>
            <strong>Город доставки - </strong>{tovar}<br>
            <strong>Продукт - </strong>{prod}<br>
            <strong>Количество - </strong>{name}<br>
            <strong>Адрес доставки - </strong>{city}<br>
            <strong>Дата доставки - </strong>{number}<br>
            <strong>Телефон - </strong>{date}<br>
            <strong>Комментарий - </strong>{comm}<br>
            <strong>Согласие на обработку данных - </strong>{counts}<br>
""")        





def create_city_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    for city in cities:
        button = types.InlineKeyboardButton(text=city, callback_data=city)
        keyboard.add(button)
    return keyboard
@dp.callback_query_handler(lambda c: c.data in cities)
async def process_city_selection(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    state = user_states.get(user_id)

    if state and state['step'] == 2:
        state['data']['tovar'] = callback_query.data  # Сохраняем выбранный город
        state['step'] += 1  # Переход на следующий шаг
        user_states[user_id] = state  # Сохраняем обновленное состояние
        if callback_query.data == "Нижний Тагил":
            await bot.send_message(chat.id, f"Вы выбрали: {callback_query.data}")
            await bot.send_message(user_id, commands.price_NT)
            # await bot.send_message(user_id, "Стоимость - Вода природная питьевая (5 л.) - цена 150 руб. (цена за 1 упак. заказ от 2 упак.)")

products = [
    "Вода природная питьевая (19 л.)",
    "Вода природная питьевая (5 л.)",
]
def create_product_keyboard():
    """Создает инлайн-клавиатуру для выбора товара."""
    keyboard1 = types.InlineKeyboardMarkup()
    for product in products:
        button = types.InlineKeyboardButton(text=product, callback_data=product)
        keyboard1.add(button)
    return keyboard1
@dp.callback_query_handler(lambda c: True)
async def process_callback_button_products(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

    print(f"Обновле: {state}")  # Отладочное сообщение

@dp.callback_query_handler(lambda c: c.data in products)
async def process_products_selection(callback_query: types.CallbackQuery):
    user_id = from_user.id
    state = (user_id)
    print('process_products_selection')

    if state and state['step'] == 8:
        user_states[user_id] = state










@bot.message_handler(func=lambda message: message.text.lower() in ["отмена", "отмена", "отменить", "отменить заявку", "отмена заявки"])
async def cancel_registration(message):
    user_id = message.from_user.id
    if user_id in user_states:
        del user_states[user_id]
        await bot.send_message(user_id, "Ваша заявка отменена")



@bot.message_handler(func=lambda message: message.text.lower() in ["оставить заявку", "/order", "order", "заказ", "заявка", "Заявка", "анкета", "заполнить анкету", "заполнить заявку", "заказать воду", "заказ воды", "оформить заказ", "оформление заказа", "заказ питьевой воды"])
async def start_registration(message):
    user_id = message.from_user.id
    user_states[user_id] = {
        'step': 1,
        'data': {}
    }
    await bot.send_message(user_id, "Если вы хотите отменить заявку, напишите 'Отменить заявку'")
    
    await bot.send_message(user_id, "Введите фамилию или название организации:")
    
    

@bot.message_handler(func=lambda message: message.from_user.id in user_states)

async def handle_registration_steps(message):
    user_id = message.from_user.id  # Получаем user_id
    state = user_states.get(user_id, {'step': 1, 'data': {}})  # Получаем состояние пользователя или создаем новое # Проверяем текущий шаг регистрации
    
    # if message.text == "отмена" or "Отмена":
    #     del user_states[user_id]
    #     await bot.send_message(user_id, "Ваша заявка отмевввнена")

    if state['step'] == 1:
        state['data']['id'] = message.text  # Сохраняем имя 
        state['step'] += 1
       

        keyboard = create_city_keyboard()
        await bot.send_message(user_id, "Выберите город доставки:", reply_markup=keyboard)
    elif state['step'] == 3:
        
        state['data']['name'] = message.text  # Сохраняем фамилию 
        state['step'] += 1
        
        await bot.send_message(user_id, "Введите адрес доставки:")
    
    elif state['step'] == 4:
        state['data']['city'] = message.text  # Сохраняем номер 
        state['step'] += 1
       
        await bot.send_message(user_id, "Введите дату доставки:")

          
    elif state['step'] == 6:
            state['data']['date'] = message.text  # Сохраняем дату 
            state['step'] += 1

            await bot.send_message(user_id, 'Введите комментарий к заказу. Если комментария нету, напишите "нет":')

    elif state['step'] == 7:

            state['data']['comm'] = message.text  # Сохраняем дату 
            state['step'] += 1
            keyboard = create_sogl_keyboard()

    
            

            await bot.send_message(user_id, "Введите согласие на обработку персональных данных(Согласен(а)/Не согласен(а)):", reply_markup=keyboard)
    















#Data base -------------------
# conn = sqlite3.connect(r'C:/Program Files/SQLiteStudio/db', check_same_thread=False)
# cursor = conn.cursor()
# def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
# 	cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
# 	conn.commit()
# @bot.message_handler(commands=['start'])
# def start_message(message):
# 	bot.send_message(message.chat.id, 'Добро пожаловать')
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
# 	if message.text.lower() == '1':
# 		bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!')
		
# 		us_id = message.from_user.id
# 		us_name = message.from_user.first_name
# 		us_sname = message.from_user.last_name
# 		username = message.from_user.username
		
# 		db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
# 		print(us_name, username)
# bot.polling(none_stop=True)

#Data base ------------------






    
    
    
    



    
    
    
    
    
    
    
    
    
    
   
