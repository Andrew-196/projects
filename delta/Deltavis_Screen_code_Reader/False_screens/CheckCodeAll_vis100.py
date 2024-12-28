import cv2
import pytesseract
import pyscreenshot as ImageGrab
import numpy as np
import pyautogui
import os
import time
import sys
import datetime
from PIL import ImageGrab
from time import sleep
from PIL import Image
import timeit
from datetime import datetime
from time import sleep
from pyautogui import ImageNotFoundException
# TIME = datetime.now().strftime("%d-%m-%Y_%H_%M_%S_%f")


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
product_type = input('Напишите название продукции: ')
print(product_type)
a = 1
b = 1
name = 'screenshot'
name_folder = datetime.now().strftime("%d-%m-%Y_%H_%M_%S_%f")
create_folder = os.mkdir(f"C:/Users/User/Desktop/Deltavis_Screen_code_Reader/{product_type, name_folder}")

while True:
   
    TIME = datetime.now().strftime("%d-%m-%Y_%H_%M_%S_%f")
    
    try:
        if pyautogui.locateOnScreen(r"C:/Users/User/Desktop/Deltavis_Screen_code_Reader/False_screens/vis100.png", confidence=0.5):
                pyautogui.screenshot(region=(1000,220, 151, 68)).save(r"C:/Users/User/Desktop/Deltavis_Screen_code_Reader/False_screens/screen_1.png")
                # region=(1000,220, 151, 68)) позиционирование на экране. Проверка на изменение
                image = Image.open(r"C:/Users/User/Desktop/Deltavis_Screen_code_Reader/False_screens/screen_1.png") #triggered 2
                string1 = pytesseract.image_to_string(image)
                
                if string != string1:
                    name = f'C:/Users/User/Desktop/Deltavis_Screen_code_Reader/{product_type, name_folder}/{TIME}.png'
                    screen = ImageGrab.grab()
                    screen.save(name, 'PNG')
                    print('save: screenshot', a, '.png')
                    
                    print(string1, "string_one_in_try")
                    print(string, "string_1_one")
                    a += 1  
                    pyautogui.screenshot(region=(1000,220, 151, 68)).save(r"C:/Users/User/Desktop/Deltavis_Screen_code_Reader/False_screens/screen_0.png")
                    # region=(1000,220, 151, 68)) позиционирование на экране. Проверка на изменение
                    image = Image.open(r"C:/Users/User/Desktop/Deltavis_Screen_code_Reader/False_screens/screen_0.png") # ,было s1.png
                    string = pytesseract.image_to_string(image)
                    
                    print(string, "string_2_screen")

        
        if string == string1:
            print("screen_0 == screen_1")
 
    except ImageNotFoundException:
        
        check = pyautogui.screenshot(region=(1000,220, 151, 68)).save(r"C:/Users/User/Desktop/Deltavis_Screen_code_Reader/False_screens/screen_0.png")
        # region=(1000,220, 151, 68)) позиционирование на экране. Проверка на изменение
        image = Image.open(r"C:/Users/User/Desktop/Deltavis_Screen_code_Reader/False_screens/screen_0.png") #triggered 1
        string = pytesseract.image_to_string(image)
        # print(a ,"no found")
        time.sleep(0.1)    
        a += 1
        print(string, 'Not found')
       
  
















