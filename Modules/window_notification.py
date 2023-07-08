from plyer import notification


class WindowNotification:
    def __init__(self):
        self.push(message="Рад вас приветствовать!")

    def push(self, message: str, timeout: int = 1):
        # Отправка уведомления
        notification.notify(
            title='Заголовок уведомления',
            message=message,
            # timeout=timeout  # Время показа уведомления в секундах
        )

