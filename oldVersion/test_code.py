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

# second
# import tkinter as tk
#
# class NotificationWindow:
#     def __init__(self, text):
#         self.root = tk.Tk()
#         self.root.overrideredirect(True)
#         self.root.geometry("+{}+{}".format(self.root.winfo_screenwidth(), 0))
#
#         # Получение высоты экрана
#         screen_height = self.root.winfo_screenheight()
#
#         self.label = tk.Label(self.root, text=text, fg="white", bg="black", font=("Arial", 14))
#         self.label.pack(fill=tk.BOTH, expand=True)
#
#         # Установка размеров окна
#         window_width = 300  # Ширина окна
#         self.root.geometry("{}x{}+{}+{}".format(window_width, screen_height, self.root.winfo_screenwidth() - window_width, 0))
#
#         self.root.configure(bg="black")  # Установка темного фона
#
#         # Установка окна поверх других окон
#         self.root.wm_attributes('-topmost', 1)
#
#     def show(self):
#         # self.root.after(8000, self.hide)  # Скрыть окно через 8 секунд
#         self.root.mainloop()
#
#     def hide(self):
#         self.root.destroy()
#
# # Пример использования:
# text = "Привет, это уведомление!"
# notification = NotificationWindow(text)
# notification.show()
#

# third
import pyautogui
# pyautogui.confirm('Shall I proceed?')
pyautogui.confirm(text='Привет', title='Ассистент', buttons=['OK', 'Cancel'])
# pyautogui.confirm(text='Привет2', title='Ассистент', buttons=['OK', 'Cancel'])
