# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


from kivy.core.window import Window

from turtle import *

class MyApp(App):


    t = Turtle()
    bgcolor("black")
    t.pencolor("purple")
    t.speed(0)
    for i in range(340):
        t.circle(190 - i, 90)
        t.left(90)
        t.circle(190 - i, 90)
        t.left(18)
        if i > 190:
            t.pensize(3)

    mainloop()

# Запуск проекта
if __name__ == "__main__":
    MyApp().run()