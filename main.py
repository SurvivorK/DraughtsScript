import win32gui
import numpy
from PIL import ImageGrab
import cv2
import time

class_name = 'Chrome_WidgetWin_0'
title_name = '弈战'

hwnd = win32gui.FindWindow(class_name, title_name)
if hwnd:
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bottom)

    for i in range(10):
        time.sleep(1)
        rect = (left, top, right, bottom)
        img = ImageGrab.grab().crop(rect)
        img.save('img.png')