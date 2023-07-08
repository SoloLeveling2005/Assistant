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
        self.BASE_DIR = ""
        self.modules = []

    def add_module(self, module):
        # Название модели будет зависеть от названия класса.
        module_name = module.__class__.__name__
        self.modules.append({
            'name': module_name,
            'module': module
        })


