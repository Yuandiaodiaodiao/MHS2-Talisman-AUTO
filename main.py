# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import numpy as np
import cv2
import matplotlib.pyplot as plt
from get_game import get_GAME
from keyboardsim import press_str, pressdownfor_str

from cnocr import CnOcr
from utils import castimg


def perpareimg(img,show=False):
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img720p = cv2.resize(img, (1280, 720))
    # img=cv2.cvtColor(img,cv2.COLOR_BGRA2RGB)
    imggray = img720p
    if show:
        plt.subplot(221)
        plt.imshow(imggray)

    h, w = imggray.shape[0:2]
    argmap = [0.35, 0.7, 0.35, 0.65]
    img_code_matrix = castimg(imggray, argmap, h, w)
    if show:
        plt.subplot(222)
        plt.imshow(img_code_matrix)
        plt.show()
    return img_code_matrix

ocr = CnOcr()
def solveOnce():
    print("启动")
    img = get_GAME()
    img = perpareimg(img)

    res = ocr.ocr(img)
    print(res)
    return "".join(res[0])


def into_point():
    pressdownfor_str('w', 4)
    pressdownfor_str('a', 5)
    pressdownfor_str('w', 6)
    pressdownfor_str('a', 0.63)
    pressdownfor_str('w', 1)
    press_str('f')
    pressdownfor_str('w', 0.05)
    press_str('f')
    pressdownfor_str('w', 0.05)
    press_str('f')

def getintoGame():
    # 任意键
    press_str('enter')
    time.sleep(3)
    # 继续游戏
    press_str('enter')
    time.sleep(2)

    press_str('s')
    time.sleep(0.7)
    press_str('enter')
    time.sleep(1)
    press_str('enter')
    time.sleep(15)
    press_str('m')
    time.sleep(1)
    press_str('z')
    time.sleep(0.7)
    press_str('d')
    time.sleep(1)
    press_str('enter')
    time.sleep(13)

    into_point()

    getcat()
    press_str('enter')
    time.sleep(1)
def getcat():


    time.sleep(1)
    press_str('enter')
    time.sleep(1)
    press_str('enter')
    time.sleep(1)
    press_str('enter')
    time.sleep(1)
    press_str('enter')
    time.sleep(2)

    press_str('w')
    time.sleep(0.7)
    press_str('enter')
    time.sleep(1)
    press_str('e')
    time.sleep(1)
    press_str('enter')
    time.sleep(0.7)
    press_str('z')
    time.sleep(1)

def backtomain2():
    time.sleep(1.5)
    press_str("esc")
    for i in range(5):
        time.sleep(0.5)
        press_str("esc")

    time.sleep(2)
    press_str("enter")
    time.sleep(1)
def backtomain():
    time.sleep(1)
    press_str("esc")
    time.sleep(1)
    press_str("w")
    time.sleep(0.7)
    press_str("a")
    time.sleep(0.7)
    press_str("enter")
    time.sleep(0.7)
    press_str("s")
    time.sleep(0.7)
    press_str("enter")
    time.sleep(0.7)
    press_str("s")
    time.sleep(0.7)
    press_str("enter")
    time.sleep(10)
from argsolver import targetsArray

def solve():
    while True:
        backtomain()
        getintoGame()
        from argsolver import args
        times = args.times

        for i in range(times):
            time.sleep(1)
            res = solveOnce()
            with open('l.txt','a',encoding='utf-8')as f:
                f.write(res)
                f.write('\n')
            print(res)
            from logger import logger
            logger.info(res)
            for target1,target2 in targetsArray:
                if target1 in res and target2 in res:
                    print("找到辣")
                    exit(0)
                    raise Exception
            press_str("enter")
        #回去
        backtomain2()
        print("main")

if __name__ == '__main__':
    from keyboard_listener import KListener

    l = KListener()
    l.bindKeyAsync('f8', solve)
    l.bindKeyAsync('f9', solveOnce)
    l.bindKeyAsync('f7', getintoGame)
    l.bindKeyAsync('f6', backtomain)
    l.join()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
