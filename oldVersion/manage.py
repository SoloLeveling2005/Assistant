import time

from Core.core import Core
# from Modules import window_notification
import os
import importlib
import threading

core = Core()
core.BASE_DIR = os.getcwd()


def scan_modules():
    """
    Сканируем папку modules и получаем все классы с их файлов и записываем их в ядро.
    """
    modules_dir = core.BASE_DIR + "/Modules"
    file_names = []
    for module_name in os.listdir(modules_dir):
        module_path = os.path.join(modules_dir, module_name)
        if os.path.isdir(module_path):
            if module_name != "__pycache__":
                file_names.append(module_name)

    classes = []
    for file_name in file_names:
        print("Modules." + file_name + ".manage")
        # module_name = file_name[:-3]  # Удаляем расширение файла ".py"
        module = importlib.import_module("Modules." + file_name + ".main")

        # Получаем все глобальные имена в модуле
        module_globals = module.__dict__

        # Итерируем по именам и проверяем их тип
        for name in module_globals:
            obj = module_globals[name]

            # Проверяем, является ли объект классом
            if isinstance(obj, type):
                classes.append(obj)

    # Теперь в массиве classes содержатся все классы из файлов
    # Можно выполнить нужные операции с ними
    print(classes)
    for cls in classes:
        # def start(core_):
        #     cls(core_)
        #     print('Hi')

        core.add_module(cls)

        # threading.Thread(target=start, args=(core,)).start()


while True:
    time.sleep(1)
