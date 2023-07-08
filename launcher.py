from Core.main import Core
from Modules import window_notification
import os
from plyer import notification

core = Core()
core.BASE_DIR = os.getcwd()

window_notification = window_notification.WindowNotification()

core.add_module(window_notification)

notification.notify(
    title='Заголовок уведомления',
    message="message",
    # timeout=timeout  # Время показа уведомления в секундах
)