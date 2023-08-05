# This is a sample Python script.
from bot import dp

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
