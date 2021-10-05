import numpy as np
import pyautogui
import cv2
import os
import keyboard
from loguru import logger as log

size = pyautogui.size()
name_file = 'screenshots/'

if not os.path.exists(name_file):
    os.mkdir(name_file)

len_list = len(os.listdir(name_file))

def doings_image():
    global name_file, size, len_list
    image = pyautogui.screenshot(region=(0,0, size[0], size[1]))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    len_list += 1
    
    name_f = name_file+f"{len_list}.png"
    log.debug(f"Создал файл {name_f}")
    cv2.imwrite(name_f, image)
    
if __name__ == "__main__":
    #print('work')
    #print(name_file)
    #print(size)
    
    keyboard.add_hotkey('Alt', doings_image)
    keyboard.wait('Ctrl + Q')