from datetime import datetime
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import *
import re

# Инициализация бота и диспетчера
bot = Bot(token='5838852905:AAHT9c3S23A1V_rDTsNc73_B-MPQVhbBNAM')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Включаем логирование
logging.basicConfig(level=logging.INFO)


# Команда /start
@dp.message_handler(Command('start'))
async def cmd_start(message: types.Message):
    # Создаем клавиатуру с кнопками
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    menu_button = types.InlineKeyboardButton("Меню 📖", callback_data='menu')
    book_button = types.InlineKeyboardButton("Забронировать столик 📅", callback_data='book')
    delivery_button = types.InlineKeyboardButton("Доставка 🚚", callback_data='delivery')
    support_button = types.InlineKeyboardButton("Поддержка 💬", callback_data='support')
    keyboard.add(menu_button, book_button, delivery_button, support_button)

    # Отправляем сообщение с клавиатурой пользователю
    await message.answer("Добро пожаловать! Что вы хотите сделать?", reply_markup=keyboard)

    # Отменяем все состояния
    await dp.current_state().reset_state(with_data=False)


# Обработчик кнопки "Меню"
@dp.callback_query_handler(text='menu')
async def process_menu(callback_query: types.CallbackQuery):
    # Получаем список типов блюд из базы данных
    categories = get_categories()

    # Разбиваем список на пары элементов
    pairs = [categories[i:i+2] for i in range(0, len(categories), 2)]

    # Создаем клавиатуру с кнопками категорий
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for pair in pairs:
        buttons = [types.KeyboardButton(category) for category in pair]
        keyboard.row(*buttons)

    # Отправляем сообщение с клавиатурой пользователю
    await callback_query.message.answer("Выберите категорию:", reply_markup=keyboard)

    # Устанавливаем следующий обработчик сообщений
    await MenuSelection.category.set()


# Состояние выбора блюда
class MenuSelection(StatesGroup):
    category = State()
    dish = State()
    table_number = State()
    payment_method = State()
    dish_id = State()


# Обработчик выбора категории блюд
@dp.message_handler(state=MenuSelection.category)
async def process_dish_category(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        # Если получено сообщение с командой, перейти в обработчик команды
        await cmd_start(message)
        return

    async with state.proxy() as data:
        data['category'] = message.text

        # Получаем список категорий блюд из базы данных
        categories = get_categories()

        # Проверяем, что выбранная категория соответствует базе данных
        if message.text not in categories:
            await message.answer("Неверная категория блюд. Выберите категорию из предложенных.")
            return

    # Получаем список блюд выбранной категории
    dishes = get_dishes_by_category(message.text)

    # Создаем клавиатуру с кнопками блюд
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    # Добавляем кнопки блюд с символами новой строки
    for dish_id, dish_name in dishes:
        keyboard.add(types.KeyboardButton(str(dish_id) + ' - ' + dish_name))

    # Отправляем сообщение с клавиатурой пользователю
    await message.answer("Выберите блюдо из категории {}:".format(message.text), reply_markup=keyboard)

    # Устанавливаем следующий обработчик сообщений
    await MenuSelection.dish.set()


# Обработчик выбора блюда
@dp.message_handler(state=MenuSelection.dish)
async def process_dish_selection(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        # Если получено сообщение с командой, перейти в обработчик команды
        await cmd_start(message)
        return

    async with state.proxy() as data:
        data['dish'] = message.text

    # Извлекаем id выбранного блюда
    dish_id = int(message.text.split()[0])

    # Получаем информацию о блюде по его id
    dish = get_dish_by_id(dish_id)

    if dish:
        # Извлекаем информацию о блюде
        dish_name = dish[1]
        ingredients = dish[3]
        price = dish[4]
        availability = dish[5]

        # Формируем сообщение с информацией о блюде
        dish_info = "🍽\nНазвание: {}\nИнгредиенты: {}\nЦена: {}\nНаличие: {}".format(dish_name, ingredients, price,
                                                                                  availability)

        # Формируем текст сообщения с информацией о блюде и кнопками выбора действия
        message_text = "{}\n\nВыберите следующее действие:".format(dish_info)

        # Создаем клавиатуру с кнопками выбора действия
        keyboard = types.InlineKeyboardMarkup()
        category_button = types.InlineKeyboardButton("Выбрать категорию", callback_data="select_category")
        order_dish_button = types.InlineKeyboardButton("Заказать блюдо", callback_data=f"order_dish {dish_id}")
        keyboard.add(category_button, order_dish_button)

        # Отправляем сообщение с информацией о блюде и кнопками выбора действия
        await message.answer(message_text, reply_markup=keyboard)
    else:
        # Если блюдо не найдено, отправляем сообщение об ошибке
        await message.answer("Блюдо не найдено")

    # Сбрасываем состояние
    await state.finish()


# Обработчик кнопки "Выбрать категорию"
@dp.callback_query_handler(text='select_category')
async def process_select_category(callback_query: types.CallbackQuery):
    # Получаем список типов блюд из базы данных
    categories = get_categories()

    # Разбиваем список на пары элементов
    pairs = [categories[i:i + 2] for i in range(0, len(categories), 2)]

    # Создаем клавиатуру с кнопками категорий
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for pair in pairs:
        buttons = [types.KeyboardButton(category) for category in pair]
        keyboard.row(*buttons)

    # Отправляем сообщение с клавиатурой пользователю
    await callback_query.message.answer("Выберите категорию:", reply_markup=keyboard)

    # Устанавливаем следующий обработчик сообщений
    await MenuSelection.category.set()


# Обработчик кнопки "Заказать блюдо"
@dp.callback_query_handler(lambda c: c.data.startswith('order_dish'))
async def process_order_dish(callback_query: types.CallbackQuery, state: FSMContext):
    dish_id = int(callback_query.data.split()[1])

    # Сохраняем выбранный dish_id в состоянии
    async with state.proxy() as data:
        data['dish_id'] = dish_id

    # Запрашиваем у пользователя номер столика
    await callback_query.message.answer("Введите номер столика:")
    await MenuSelection.table_number.set()


# Обработчик ввода номера столика
@dp.message_handler(state=MenuSelection.table_number)
async def process_table_number(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return

    table_number = message.text

    # Проверяем, что введенное значение является цифрой от 1 до 20
    if not table_number.isdigit() or not (1 <= int(table_number) <= 20):
        await message.answer("Неверный номер столика. У нас 20 столов.")
        return

    # Получаем текущую дату и время
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Создаем клавиатуру с кнопками выбора способа оплаты
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cash_button = types.KeyboardButton("Наличные")
    card_button = types.KeyboardButton("Карта")
    keyboard.add(cash_button, card_button)

    # Запрашиваем у пользователя информацию о способе оплаты
    await message.answer("Выберите способ оплаты:", reply_markup=keyboard)
    await MenuSelection.payment_method.set()
    await state.update_data(table_number=table_number, datetime=current_datetime)


# Обработчик выбора способа оплаты
@dp.message_handler(state=MenuSelection.payment_method)
async def process_payment_method(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    payment_method = message.text

    if payment_method == 'Наличные':
        payment_info = 'Наличные'
    elif payment_method == 'Карта':
        payment_info = 'Карта'
    else:
        await message.answer("Неверный выбор способа оплаты.")
        return

    async with state.proxy() as data:
        table_number = data['table_number']
        datetime = data['datetime']
        dish_id = data['dish_id']

    # Добавляем информацию о заказе в таблицу Заказы
    order_id = add_order(table_number, datetime, payment_info)

    # Добавляем информацию о блюде в таблицу Заказы_Блюда
    add_dish_to_order(order_id, dish_id)

    await message.answer("Ваш заказ успешно оформлен!")
    await message.answer("Скоро к вам подойдёт официант для оплаты заказа")

    # Сбрасываем состояние
    await state.finish()


# Определение состояний FSM
class TableBooking(StatesGroup):
    TYPE = State()          # Выбор типа столика
    TABLE = State()         # Выбор столика
    PHONE = State()         # Ввод номера телефона
    NAME = State()          # Ввод имени
    SURNAME = State()       # Ввод фамилии
    DATE = State()          # Выбор даты бронирования


@dp.callback_query_handler(lambda call: call.data == 'book')
async def handle_book(callback_query: types.CallbackQuery):
    # Отправляем сообщение с запросом выбора типа столика
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[types.KeyboardButton(type) for type in ['VIP', 'В зале', 'У окна']])
    await bot.send_message(callback_query.message.chat.id, "Какой тип столика вы хотите?", reply_markup=keyboard)

    # Устанавливаем следующий обработчик сообщений
    await TableBooking.TYPE.set()


@dp.message_handler(state=TableBooking.TYPE)
async def handle_table_type(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    async with state.proxy() as data:
        data['table_type'] = message.text

    # Получаем информацию о столиках по выбранному типу из базы данных
    tables = get_tables_by_type(message.text)

    if tables:
        # Формируем сообщение с информацией о столах
        table_info = "Доступные столы:\n\n"
        for table in tables:
            table_number = table[0]
            table_seats = table[2]
            table_price = table[3]
            table_info += "🍽 Столик {}: Места: {}, Цена: {} руб.\n".format(table_number, table_seats, table_price)

        # Формируем текст сообщения с информацией о столах и кнопкой выбора столика
        message_text = "{}\n\nВыберите столик:".format(table_info)

        # Создаем клавиатуру с кнопками выбора столика
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttons = [types.KeyboardButton(str(table[0])) for table in tables]
        keyboard.add(*buttons)

        # Отправляем сообщение с информацией о столах и кнопками выбора столика
        await message.answer(message_text, reply_markup=keyboard)

        # Устанавливаем следующий обработчик сообщений
        await TableBooking.TABLE.set()
    else:
        # Если столики не найдены, отправляем сообщение об ошибке
        await message.answer("Извините, столики данного типа не доступны 😔")


@dp.message_handler(state=TableBooking.TABLE)
async def handle_table_selection(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    async with state.proxy() as data:
        data['selected_table'] = message.text

    await message.answer("Для бронирования столика необходимо ввести ваше имя, фамилию и номер телефона.")
    # Запрашиваем у пользователя номер телефона
    await message.answer("Введите номер в формате +X (XXX) XXX-XXXX, где X - цифра.")
    await TableBooking.PHONE.set()


@dp.message_handler(state=TableBooking.PHONE)
async def handle_phone_number(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    phone_number = message.text.strip()

    # Проверяем формат номера телефона
    pattern = r'^[78]\d{10}$'
    if not re.match(pattern, phone_number):
        await message.answer("Неверный формат номера телефона. Введите номер в формате +X (XXX) XXX-XXXX, где X - цифра.")
        return

    async with state.proxy() as data:
        data['phone_number'] = phone_number

    # Запрашиваем у пользователя имя
    await message.answer("Введите ваше имя:")
    await TableBooking.NAME.set()


@dp.message_handler(state=TableBooking.NAME)
async def handle_name(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return

    name = message.text

    # Проверяем, что введенное значение содержит только буквы
    if not name.isalpha():
        await message.answer("Неверный формат имени. Имя должно состоять только из букв.")
        return

    async with state.proxy() as data:
        data['name'] = message.text

    # Запрашиваем у пользователя фамилию
    await message.answer("Введите вашу фамилию:")
    await TableBooking.SURNAME.set()


@dp.message_handler(state=TableBooking.SURNAME)
async def handle_surname(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return

    surname = message.text

    # Проверяем, что введенное значение содержит только буквы
    if not surname.isalpha():
        await message.answer("Неверный формат фамилии. Фамилия должна состоять только из букв.")
        return

    async with state.proxy() as data:
        data['surname'] = message.text

    # Запрашиваем у пользователя дату бронирования столика
    await message.answer("На какую дату и время вы хотите забронировать столик?(Формат:ДД.ММ.ГГГГ ЧЧ:ММ)")
    await TableBooking.DATE.set()


@dp.message_handler(state=TableBooking.DATE)
async def handle_booking_date(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    async with state.proxy() as data:
        data['booking_date'] = message.text

    booking_date = data['booking_date']

    try:
        # Пытаемся преобразовать введенную дату в формат datetime
        booking_date = datetime.datetime.strptime(booking_date, "%d.%m.%Y %H:%M")

        # Проверяем, что выбранный столик не забронирован в выбранное время
        table_available = check_table_availability(data['selected_table'], booking_date)
        if not table_available:
            await message.answer("Выбранный столик уже забронирован в указанное время."
                                 "(Вы можете забронировать столик только на 45 минут вперед или назад)")
            await TableBooking.DATE.set()
            return

        # Вызываем функцию для бронирования столика
        book_table(data['selected_table'], booking_date, data['phone_number'], data['name'], data['surname'])

        # Получаем информацию о забронированном столике
        table_info = get_table_info(data['selected_table'])

        if table_info:
            # Извлекаем информацию о столике
            table_number = table_info[0]
            table_type = table_info[1]
            table_seats = table_info[2]
            table_price = table_info[3]

            # Формируем сообщение с информацией о забронированном столике
            booking_info = "Ваш столик: {}\nДата бронирования: {}\nТип стола: {}\nКоличество мест: {}\nЦена: {}".format(
                table_number, booking_date, table_type, table_seats, table_price)

            # Создаем объект InlineKeyboardMarkup для отображения кнопок
            keyboard = types.InlineKeyboardMarkup()

            # Создаем кнопки "Отменить" и "Изменить" с соответствующими callback_data
            cancel_button = types.InlineKeyboardButton("Отменить", callback_data="cancel")
            modify_button = types.InlineKeyboardButton("Изменить", callback_data="modify")

            # Добавляем кнопки в клавиатуру
            keyboard.add(cancel_button, modify_button)

            # Отправляем сообщение с подтверждением бронирования, информацией о столике и кнопками
            await message.answer("Столик успешно забронирован!\n\n{}".format(booking_info), reply_markup=keyboard)

        else:
            # Если информация о столике не найдена, отправляем сообщение об ошибке
            await message.answer("Ошибка при получении информации о столике")
    except ValueError:
        # Если происходит исключение ValueError при парсинге даты
        await message.answer("Некорректный формат даты. Пожалуйста, введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ")
        await TableBooking.DATE.set()


# Обработчик отмены бронирования
@dp.callback_query_handler(lambda call: call.data == 'cancel', state='*')
async def handle_cancel(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        selected_table = data.get('selected_table')
        booking_date = data.get('booking_date')

        if selected_table and booking_date:
            # Удалить запись о бронировании из базы данных
            cancel_booking(selected_table, booking_date)

            # Отправить сообщение об отмене бронирования
            await callback_query.answer("Вы отменили бронирование")
        else:
            # Если информация о столике и дате бронирования отсутствует,
            # просто удалить сообщение
            await callback_query.message.delete()

    await state.finish()


# Обработчик кнопки "Изменить"
@dp.callback_query_handler(lambda call: call.data == 'modify', state=TableBooking.DATE)
async def handle_modify(callback_query: types.CallbackQuery, state: FSMContext):
    # Получаем данные из состояния FSM
    async with state.proxy() as data:
        selected_table = data['selected_table']
        booking_date = data['booking_date']

    # Запрашиваем у пользователя новую дату бронирования
    await callback_query.message.answer("Введите новую дату и время бронирования (Формат: ДД.ММ.ГГГГ ЧЧ:ММ):")
    await TableBooking.DATE.set()

    # Сохраняем выбранный столик и старую дату бронирования в контексте состояния
    async with state.proxy() as data:
        data['selected_table'] = selected_table
        data['booking_date'] = booking_date


# Обработчик новой даты бронирования после нажатия кнопки "Изменить"
@dp.message_handler(state=TableBooking.DATE)
async def handle_modify_date(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    # Получаем данные из состояния FSM
    async with state.proxy() as data:
        selected_table = data['selected_table']
        booking_date = data['booking_date']
        new_date = message.text

    try:
        # Пытаемся преобразовать введенную дату в формат datetime
        new_date = datetime.datetime.strptime(new_date, "%d.%m.%Y %H:%M")

        # Вызываем функцию для обновления даты бронирования
        update_booking(selected_table, booking_date, new_date)

        # Отправляем сообщение об успешном обновлении
        await message.answer("Дата бронирования успешно изменена на: {}".format(new_date))

        # Очищаем состояние FSM
        await state.finish()
    except ValueError:
        # Если происходит исключение ValueError при парсинге даты
        await message.answer("Некорректный формат даты. Пожалуйста, введите дату в формате ДД.ММ.ГГГГ ЧЧ:ММ")


# Обработчик нажатия на кнопку "Поддержка"
@dp.callback_query_handler(lambda c: c.data == 'support')
async def support(callback_query: types.CallbackQuery):
    # Формируем ссылку на профиль в Telegram
    text = f"https://t.me/HLebZy"

    # Отправляем сообщение ссылкой на профиль
    await callback_query.bot.answer_callback_query(callback_query.id)
    await callback_query.bot.send_message(callback_query.from_user.id, text)


class Delivery(StatesGroup):
    PHONE_NUMBER = State()  # Состояние для ввода номера телефона
    NAME = State()  # Состояние для ввода имени
    SURNAME = State()  # Состояние для ввода фамилии
    ADDRESS = State()  # Состояние для ввода адреса
    SELECTED_DISHES = State()  # Состояние для выбора блюд для доставки
    PAYMENT_METHOD = State()  # Состояние для выбора способа оплаты


# Обработчик кнопки "Доставка"
@dp.callback_query_handler(text='delivery')
async def process_delivery(callback_query: types.CallbackQuery):
    # Запрашиваем у пользователя информацию о доставке
    await callback_query.message.answer("Введите номер в формате +X (XXX) XXX-XXXX, где X - цифра.:")
    await Delivery.PHONE_NUMBER.set()


@dp.message_handler(state=Delivery.PHONE_NUMBER)
async def process_delivery_phone_number(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    phone_number = message.text.strip()

    # Проверяем формат номера телефона
    pattern = r'^[78]\d{10}$'
    if not re.match(pattern, phone_number):
        await message.answer("Неверный формат номера телефона. Введите номер в формате +X (XXX) XXX-XXXX, где X - цифра.")
        return

    async with state.proxy() as data:
        data['phone_number'] = phone_number

    # Запрашиваем у пользователя имя
    await message.answer("Введите ваше имя:")
    await Delivery.NAME.set()


@dp.message_handler(state=Delivery.NAME)
async def process_delivery_name(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    name = message.text.strip()

    # Проверяем, что введенное значение содержит только буквы
    if not name.isalpha():
        await message.answer("Неверный формат имени. Имя должно состоять только из букв.")
        return

    async with state.proxy() as data:
        data['name'] = name

    # Запрашиваем у пользователя фамилию
    await message.answer("Введите вашу фамилию:")
    await Delivery.SURNAME.set()


@dp.message_handler(state=Delivery.SURNAME)
async def process_delivery_surname(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    surname = message.text.strip()

    # Проверяем, что введенное значение содержит только буквы
    if not surname.isalpha():
        await message.answer("Неверный формат фамилии. Фамилия должна состоять только из букв.")
        return

    async with state.proxy() as data:
        data['surname'] = surname

    # Запрашиваем у пользователя адрес доставки
    await message.answer("Введите адрес доставки:")
    await Delivery.ADDRESS.set()



@dp.message_handler(state=Delivery.ADDRESS)
async def process_delivery_address(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    async with state.proxy() as data:
        data['address'] = message.text

        # Получаем текущую дату и время
        order_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data['order_datetime'] = order_datetime

    await show_dish_selection(message, state)


async def show_dish_selection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # Получаем список блюд из базы данных
        dishes = get_dishes()

        # Создаем текстовое сообщение с информацией о блюдах
        dish_info_message = "Выберите блюда для доставки:\n"

        for dish_info in dishes:
            dish_id = dish_info[0]
            dish_name = dish_info[1]
            dish_info = get_dish_info(dish_id)
            if dish_info:
                dish_info_message += f"{dish_id} - {dish_name}\nНазвание: {dish_info[0]}\nИнгредиенты: {dish_info[1]}\nЦена: {dish_info[2]} руб.\n\n"

        # Добавляем сообщение с инструкцией по выбору блюд
        dish_info_message += "Перечислите блюда, которые хотите заказать через пробел (Пример: 1 2 3 4 5 6 7)"

        # Отправляем сообщение с информацией о блюдах пользователю
        await message.answer(dish_info_message)

        # Устанавливаем следующий обработчик сообщений
        await Delivery.SELECTED_DISHES.set()


@dp.message_handler(state=Delivery.SELECTED_DISHES)
async def process_selected_dishes(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    async with state.proxy() as data:
        selected_dishes = []

        # Проверяем выбранные блюда
        for dish_id_str in message.text.split():
            if dish_id_str.isdigit():
                dish_id = int(dish_id_str)
                if is_dish_available(dish_id):
                    selected_dishes.append(dish_id)

        # Проверяем, что были выбраны блюда
        if not selected_dishes:
            await message.answer("Вы не выбрали ни одного доступного блюда.")
            return

        # Сохраняем выбранные блюда в состоянии
        if 'selected_dishes' in data:
            data['selected_dishes'].extend(selected_dishes)
        else:
            data['selected_dishes'] = selected_dishes

    await show_order_confirmation(message, state)


async def show_order_confirmation(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    async with state.proxy() as data:
        selected_dishes_info = []

        # Получаем информацию о выбранных блюдах
        for dish_id_str in data['selected_dishes']:
            dish_id = int(dish_id_str)
            dish_info = get_dish_info(dish_id)
            if dish_info:
                selected_dishes_info.append(f"Позиция: {dish_id}, {dish_info[0]}")

        # Отправляем подтверждение заказа с доставкой и предлагаем выбрать способ оплаты
        confirmation_message = "Ваш заказ доставки:\n\n" \
                               "Номер телефона: {}\n" \
                               "Имя: {}\n" \
                               "Фамилия: {}\n" \
                               "Адрес: {}\n" \
                               "Дата и время оформления: {}\n\n" \
                               "Выбранные блюда:\n{}".format(data['phone_number'], data['name'], data['surname'],
                                                             data['address'], data['order_datetime'],
                                                             '\n'.join(selected_dishes_info))
        await message.answer(confirmation_message)

        # Создаем клавиатуру с кнопками способов оплаты
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(types.KeyboardButton("Онлайн оплата"))
        keyboard.add(types.KeyboardButton("Оплата курьеру"))

        # Отправляем сообщение с клавиатурой пользователю
        await message.answer("Выберите способ оплаты:", reply_markup=keyboard)

        # Устанавливаем следующий обработчик сообщений
        await Delivery.PAYMENT_METHOD.set()



@dp.message_handler(state=Delivery.PAYMENT_METHOD)
async def process_payment_method(message: types.Message, state: FSMContext):
    if message.text.startswith('/'):
        await cmd_start(message)
        return
    async with state.proxy() as data:
        # Проверяем выбранный способ оплаты
        payment_method = message.text
        if payment_method not in ["Онлайн оплата", "Оплата курьеру"]:
            await message.answer("Пожалуйста, выберите один из предложенных способов оплаты.")
            return

        # Добавляем информацию о способе оплаты в состояние
        data['payment_method'] = payment_method

        # Сохраняем доставку в базе данных
        delivery_info = {
            'phone_number': data['phone_number'],
            'name': data['name'],
            'surname': data['surname'],
            'address': data['address'],
            'order_datetime': data['order_datetime'],
            'payment_method': data['payment_method']
        }
        delivery_id = add_delivery(delivery_info)

        # Добавляем выбранные блюда в заказ
        for dish_id in data['selected_dishes']:
            add_dish_to_delivery(delivery_id, dish_id)

        # Формируем сообщение с информацией о доставке и выбранных блюдах
        confirmation_message = "Ваш чек доставки:\n\n" \
                               "Номер телефона: {}\n" \
                               "Имя: {}\n" \
                               "Фамилия: {}\n" \
                               "Адрес: {}\n" \
                               "Дата и время оформления: {}\n" \
                               "Способ оплаты: {}\n\n" \
                               "Выбранные блюда:\n".format(data['phone_number'], data['name'], data['surname'],
                                                          data['address'], data['order_datetime'],
                                                          data['payment_method'])

        for dish_id in data['selected_dishes']:
            dish_info = get_dish_info(dish_id)
            if dish_info:
                dish_info_message = "Позиция: {}, {}\n".format(dish_id, dish_info[0])
                confirmation_message += dish_info_message

        # Добавляем сообщение ожидания обработки заказа
        confirmation_message += "\nВаш заказ в обработке. Скоро с вами свяжется оператор."

        await message.answer(confirmation_message)

    # Сбрасываем состояние пользователя
    await state.finish()



# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
