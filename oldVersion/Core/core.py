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
from Core.settings import CoreSettings


class Core(CoreSettings):
    def __init__(self):
        super().__init__()

    def add_module(self, module):
        """
        Добавление модуля.
        """

        # Название модели будет зависеть от названия класса.
        module_name = module.__class__.__name__
        print(module_name)
        self.modules.append({
            'name': module_name,
            'module': module
        })


