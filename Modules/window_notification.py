from plyer import notification


class WindowNotification:
    def __init__(self, core):
        self.core = core
        self.welcome_message = "Здравствуйте"
        self.welcome_title = ""
        self.push(message=self.welcome_message, title=self.welcome_title)

    def push(self, title: str, message: str, timeout: int = 1):
        # Отправка уведомления
        notification.notify(
            title=title,
            message=message,
            app_name=self.core.name,
            # app_icon=self.core.BASE_DIR + "\\Core\\assets\\logo.ico",
            timeout=timeout,
        )
