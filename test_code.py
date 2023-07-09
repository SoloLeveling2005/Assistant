# import tkinter as tk
# from tkinter import ttk
#
#
# def create_app():
#     root = tk.Tk()
#     root.overrideredirect(True)  # Убираем шапку окна
#
#     screen_width = root.winfo_screenwidth()
#     window_width = 130  # Задайте желаемую ширину окна здесь
#     x_position = screen_width - window_width - 20
#
#     root.geometry(f"{window_width}x60+{x_position}+20")  # Прижимаем окно к правому верхнему углу
#
#     # Устанавливаем стилизацию для темной темы
#     style = ttk.Style()
#     style.theme_use('clam')  # Выбираем одну из доступных тем (можно изменить)
#     style.configure('.', background='#333', foreground='#fff')  # Задаем цвета фона и текста для всех виджетов
#
#     # Создаем фрейм для виджета
#     frame = ttk.Frame(root, padding=10)
#     frame.grid(row=0, column=0, sticky='ne')
#
#     # Создаем виджет
#     label = ttk.Label(frame, text="Текст сообщения", font=('Helvetica', 12))
#     label.grid(row=0, column=0, padx=10, pady=10)
#
#     root.mainloop()
#
#
# create_app()

from winotify import Notification

toast = Notification(app_id="windows app",
                     title="Winotify Test Toast",
                     msg="New Notification!")

toast.show()




