import pyautogui
import random
from threading import Thread


def f():
    pyautogui.FAILSAFE = False
    while True:
        print("going to")
        x = random.randint(0, 1920)
        print("X:", x)
        y = random.randint(0, 1080)
        print("Y:", y)
        pyautogui.moveTo(x, y, duration = 0)


def main():

    for i in range(25):
        Thread(target=f)

    while True:
        pass


if __name__ == '__main__':
    main()
