import pyautogui
import random
import threading


def f():
    pyautogui.FAILSAFE = False
    while True:
        print("going to")
        x = random.randint(0, 1920)
        print("X:", x)
        y = random.randint(0, 1080)
        print("Y:", y)
        pyautogui.moveTo(x, y, duration=0)
        pyautogui.click()


x11 = threading.Thread(target=f())
x21 = threading.Thread(target=f())
x31 = threading.Thread(target=f())
x41 = threading.Thread(target=f())
x51 = threading.Thread(target=f())
x61 = threading.Thread(target=f())
x71 = threading.Thread(target=f())
x81 = threading.Thread(target=f())
x91 = threading.Thread(target=f())
x01 = threading.Thread(target=f())
x12 = threading.Thread(target=f())
x22 = threading.Thread(target=f())
x32 = threading.Thread(target=f())
x42 = threading.Thread(target=f())
x52 = threading.Thread(target=f())
x62 = threading.Thread(target=f())
x72 = threading.Thread(target=f())
x82 = threading.Thread(target=f())
x92 = threading.Thread(target=f())
x02 = threading.Thread(target=f())

x11.start()
x21.start()
x31.start()
x41.start()
x51.start()
x61.start()
x71.start()
x81.start()
x91.start()
x01.start()
x12.start()
x22.start()
x32.start()
x42.start()
x52.start()
x62.start()
x72.start()
x82.start()
x92.start()
x02.start()

while True:
    pass
