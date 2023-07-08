from Core.main import Core
import os
core = Core()
core.BASE_DIR = os.getcwd()
print(core.lifetime)
