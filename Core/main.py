# TODO Создать ядро приложения. Оно должно иметь функции.
# TODO - Хранение информации о ядре.
# TODO - Подключение модулей.
# TODO Создать пример модуля.
# TODO
# TODO
# TODO
# TODO

import time
import os


class Core:
    def __init__(self):
        self.username = "Solo Leveling"
        self.lifetime = time.time()
        self.path = os.path.realpath(__file__)
