from datetime import timedelta
import datetime
import mysql.connector



# Функция для установления соединения с базой данных
def connect_to_database():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        port=3306,
        password="",
        database="restaurant"
    )


# Получение списка категорий блюд
def get_categories():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Тип FROM Блюда")
    categories = [row[0] for row in cursor.fetchall()]
    conn.close()
    return categories


# Получение списка блюд в выбранной категории
def get_dishes_by_category(category):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Блюдо, Название FROM Блюда WHERE Тип = %s", (category,))
    dishes = cursor.fetchall()
    conn.close()
    return dishes


# Получение информации о блюде по его id
def get_dish_by_id(dish_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Блюда WHERE Блюдо = %s", (dish_id,))
    dish = cursor.fetchone()
    conn.close()
    return dish


# Добавление заказа
def add_order(table, date, payment_info):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Заказы (Столик, Дата, `Способ_платы`) VALUES (%s, %s, %s)", (table, date,
                                                                                                     payment_info))
    order_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return order_id


# Функция для добавления записи в таблицу Заказы_Блюда
def add_dish_to_order(order_id, dish_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Заказы_Блюда (Заказ, Блюдо) VALUES (%s, %s)", (order_id, dish_id))
    conn.commit()
    conn.close()


# Получение типа столиков
def get_tables():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Столики WHERE Тип = %s")
    tables = cursor.fetchall()
    conn.close()
    return tables


# Получение типа столиков
def get_tables_by_type(table_type):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Столики WHERE Тип = %s", (table_type,))
    tables = cursor.fetchall()
    conn.close()
    return tables


# Бронирование столика
def book_table(table, date, phone_number, name, surname):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Бронирования (Столик, Дата, Номер_телефона, Имя, Фамилия) VALUES (%s, %s, %s, %s, %s)",
                   (table, date, phone_number, name, surname))
    conn.commit()
    conn.close()


# Функция для получения информации о столике по его номеру
def get_table_info(table_number):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Столики WHERE Столик = %s", (table_number,))
    table_info = cursor.fetchone()
    conn.close()
    return table_info


# Функция для проверки доступности столика в указанное время с учетом ограничения 45 минут
def check_table_availability(table_number, booking_date):
    conn = connect_to_database()
    cursor = conn.cursor()

    # Calculate the time range for checking availability
    min_booking_time = booking_date - timedelta(minutes=44)
    max_booking_time = booking_date + timedelta(minutes=44)

    # Check if there are any bookings within the time range for the specified table
    cursor.execute("SELECT * FROM Бронирования WHERE Столик = %s AND Дата BETWEEN %s AND %s",
                   (table_number, min_booking_time, max_booking_time))
    bookings = cursor.fetchall()

    conn.close()

    return len(bookings) == 0


# Функция для отмены бронирования
def cancel_booking(table_number, booking_date):
    conn = connect_to_database()
    cursor = conn.cursor()

    # Преобразование строки даты в объект datetime
    booking_date = datetime.datetime.strptime(booking_date, "%d.%m.%Y %H:%M")

    cursor.execute("DELETE FROM Бронирования WHERE Столик = %s AND Дата = %s", (table_number, booking_date))
    conn.commit()
    conn.close()


def modify_booking(table_number, new_date):
    conn = connect_to_database()
    cursor = conn.cursor()
    # Преобразование объекта datetime в строку в нужном формате
    new_date_str = new_date.strftime("%d.%m.%Y %H:%M")
    cursor.execute("UPDATE Бронирования SET Дата = %s WHERE Столик = %s", (new_date_str, table_number))
    conn.commit()
    cursor.close()
    conn.close()


# Функция для изменения даты бронирования
def update_booking(table_number, booking_date, new_date):
    conn = connect_to_database()
    cursor = conn.cursor()
    # Преобразование старой и новой даты в объекты datetime
    booking_date = datetime.datetime.strptime(booking_date, "%d.%m.%Y %H:%M")
    new_date = datetime.datetime.strptime(new_date, "%d.%m.%Y %H:%M")

    query = "DELETE FROM Бронирования WHERE Столик = %s AND Дата = %s; \
             INSERT INTO Бронирования (Столик, Дата) VALUES (%s, %s)"
    values = (table_number, booking_date, table_number, new_date)
    cursor.execute(query, values)

    conn.commit()
    conn.close()

def get_dishes():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Блюда")
    dishes = cursor.fetchall()
    conn.close()
    return dishes


def get_dishes_by_type(dish_type):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Блюдо, Название FROM Блюда WHERE Тип = %s", (dish_type,))
    dishes = cursor.fetchall()
    conn.close()
    return dishes

def get_dish_info(dish_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Название, Ингредиенты, Цена FROM Блюда WHERE Блюдо = %s", (dish_id,))
    dish_info = cursor.fetchone()
    conn.close()

    return dish_info


# Проверка доступности блюда по его id
def is_dish_available(dish_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Блюдо FROM Блюда WHERE Блюдо = %s", (dish_id,))
    dish = cursor.fetchone()
    conn.close()
    return dish is not None


# Добавление доставки
def add_delivery(delivery_info):
    conn = connect_to_database()
    cursor = conn.cursor()

    # Получите значение для поля 'Доставка' из delivery_info или установите значение по умолчанию
    delivery = int(delivery_info.get('delivery', 0))

    cursor.execute("INSERT INTO Доставка (Номер_телефона, Имя, Фамилия, Адрес, Дата_время_оформления, Способ_оплаты_доставки, Доставка) "
                   "VALUES (%(phone_number)s, %(name)s, %(surname)s, %(address)s, %(order_datetime)s, %(payment_method)s, %(delivery)s)",
                   {'phone_number': delivery_info['phone_number'],
                    'name': delivery_info['name'],
                    'surname': delivery_info['surname'],
                    'address': delivery_info['address'],
                    'order_datetime': delivery_info['order_datetime'],
                    'payment_method': delivery_info['payment_method'],
                    'delivery': delivery})

    delivery_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return delivery_id


# Добавление блюда в доставку
def add_dish_to_delivery(delivery_id, dish_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Блюда_доставка (Доставка, Блюдо) VALUES (%s, %s)", (delivery_id, dish_id))
    conn.commit()
    conn.close()