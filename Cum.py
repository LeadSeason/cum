import pyautogui 
import random
from multiprocessing import Process

def f():
    FAILSAFE = False
    while True:
        print("going to")
        x = random.randint(0, 1920)
        print("X:",x)
        y = random.randint(0, 1080)
        print("Y:",y)
        pyautogui.moveTo(x, y, duration = 0)

def main():
    
    for i in range(int(input())):
        p = Process(target=f)
        p.start()
    p.join()

if __name__ == '__main__':
    main()
