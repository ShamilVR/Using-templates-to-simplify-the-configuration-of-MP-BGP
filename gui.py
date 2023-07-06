from tkinter import *
from jinja2 import Template
import pyperclip

# Оставьте остальную часть кода без изменений

# Функция для отображения полной конфигурации в текстовом поле
def display_config():
    global full_config
    config_text.delete(1.0, END)  # Очистка текстового поля
    config_text.insert(END, full_config)  # Вставка полной конфигурации

# Функция для настройки интерфейса через GUI
def configure_interface_gui():
    # Создание диалогового окна для ввода данных
    interface_window = Toplevel(root)
    interface_window.title("Настройка интерфейса")

    # Оставьте остальную часть функции без изменений

    # Добавление кнопки "Отобразить конфигурацию"
    show_config_button = Button(interface_window, text="Отобразить конфигурацию", command=display_config)
    show_config_button.pack()

# Создание главного окна Tkinter
root = Tk()
root.title("Настройка роутера")

# Добавление кнопки "Настроить интерфейс" в главное окно
interface_button = Button(root, text="Настроить интерфейс", command=configure_interface_gui)
interface_button.pack()

# Добавление текстового поля для отображения конфигурации
config_text = Text(root, width=50, height=10)
config_text.pack()

# Запуск главного цикла Tkinter
root.mainloop()
