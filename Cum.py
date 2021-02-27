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


for i in range(25):
    x = threading.Thread(target=f())

x.start()
while True:
    pass
