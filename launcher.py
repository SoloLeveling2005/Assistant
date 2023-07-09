import time

from Core.main import Core
# from Modules import window_notification
import os
import importlib


core = Core()
core.BASE_DIR = os.getcwd()

# window_notification = window_notification.WindowNotification(core)

# core.add_module(window_notification)

modules_dir = core.BASE_DIR+"/Modules"
file_names = []
for module_name in os.listdir(modules_dir):
    module_path = os.path.join(modules_dir, module_name)
    if os.path.isdir(module_path):
        if module_name != "__pycache__":
            file_names.append(module_name)
print(file_names)

classes = []

for file_name in file_names:
    print("Modules."+file_name+".manage")
    # module_name = file_name[:-3]  # Удаляем расширение файла ".py"
    module = importlib.import_module("Modules."+file_name+".manage")

    # Получаем все глобальные имена в модуле
    module_globals = module.__dict__

    # Итерируем по именам и проверяем их тип
    for name in module_globals:
        print(name)
        obj = module_globals[name]

        # Проверяем, является ли объект классом
        if isinstance(obj, type):
            if (obj)
            classes.append(obj)

# Теперь в массиве classes содержатся все классы из файлов
# Можно выполнить нужные операции с ними
for cls in classes:
    print(cls)


while True:
    time.sleep(1)
