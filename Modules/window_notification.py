from plyer import notification

class WindowNotification:
    def __init__(self, core):
        self.core = core
        self.push(message="Рад вас видеть!", title="1")

    def push(self, title: str, message: str, timeout: int = 1):
        print(self.core.BASE_DIR)
        # Отправка уведомления
        notification.notify(
            title=title,
            message=message,
            app_name=self.core.username,
            app_icon=self.core.BASE_DIR+"\\Core\\assets\\logo.ico",
            timeout=timeout,
            # ticker
            # timeout=timeout  # Время показа уведомления в секундах
        )
