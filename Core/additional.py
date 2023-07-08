import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 140)  # Настройка скорости речи (по умолчанию 200)
engine.setProperty('volume', 1)  # Настройка громкости речи (от 0.0 до 1.0)


text = """Hi. The user is being registered. What is your name?"""
engine.say(text)
engine.runAndWait()
