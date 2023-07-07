import numpy as np
import pyautogui
import cv2
import os
import keyboard
from datetime import datetime

class Screenshot:
    
    def __init__(self):
        self.size = pyautogui.size()
        self.dir_name = 'screenshots'

    def pathExists(self):
        """Проверяем, что папка, куда будет сохранен
        скриншот - существует!
        Если ее нет, то создаем ее
        """
        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)
            
    def do_screenshot(self):
        """Создаем снимок экрана"""
        image = pyautogui.screenshot(region=(0,0, self.size[0], self.size[1]))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        return image
        
    def save(self, image):
        """Сохраняем картинку по указанному пути"""
        now = datetime.now()
        name_file = f"{self.dir_name}/{now.strftime('%d_%m_%Y_%H_%M_%S')}.png"
        cv2.imwrite(name_file, image)
        
        print(f"Сохранил скриншот в файл: {name_file}")

    def screenshoted(self):
        self.pathExists()
        image = self.do_screenshot()
        self.save(image)

class Events():
    
    
    def __init__(self, func_screen):
        self.screenshot = "alt"
        self.end = "q"
        self.wait_events_work = True
        
        self.screenshoted = func_screen
        
        self.events = []

    def event_do(self):
        """Выполняем вызванные пользователем события(event)"""
        for event in self.events:
            if event == self.screenshot:
                self.screenshoted()
                
            elif event == self.end:
                    self.wait_events_work = False
            else:
                pass
                # print(f'Error: Команды {event} не существует!')
                
        self.events = []

    def wait_events(self):
        """Начинаем отлавливать события(нажатия клавиш), которые вызвал пользователь"""
        while self.wait_events_work:
            event = keyboard.read_event()
            self.events.append(event.name)
            self.event_do()
        
    
if __name__ == "__main__":
    print(f'Programm start!\nDo screenshot press alt\nEnd screenshoted press q')
    screenshot = Screenshot()
    event = Events(screenshot.screenshoted)
    event.wait_events()
    print(f'Programm END!')