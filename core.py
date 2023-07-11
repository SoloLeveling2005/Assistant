import time

from plyer import notification


class Assistant:
    def __init__(self):
        # Имя ассистента
        self.name = "SoloLeveling"

        # Отправляем уведомление о запуске ассистента
        notification.notify(
            title="",
            message="Здравствуйте",
            timeout=4,
        )

        # TODO Сделать верстку.
