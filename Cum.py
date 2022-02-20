import pyautogui
import random
from multiprocessing import Process
from multiprocessing import cpu_count
from threading import Thread


def f():
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0.1

    while True:
        print("going to")
        x = random.randint(0, 1920)
        print("X:", x)
        y = random.randint(0, 1080)
        print("Y:", y)
        pyautogui.moveTo(x, y, duration=0)
        pyautogui.click()


def main():
    for _ in range(1):
        p = Process(target=f)
        p.start()
    p.join()


if __name__ == '__main__':
    main()
