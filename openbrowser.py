#openbrowser.py

import pyautogui #เมา+คีบอด controll
import  time # เวลา
import  webbrowser 
import pyperclip # คัดลอก + วาง

url = 'https://www.google.com'

webbrowser.open(url)
time.sleep(3)

pyautogui.click(394,51)
pyautogui.typewrite('thailand')
pyautogui.press('enter')

def Search(word):
    time.sleep(3)
    for i in range(7):              
        pyautogui.press('tab')
    pyautogui.press('backspace')
    pyautogui.typewrite(word,interval=0.2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.screenshot(word + '.png')
   
Search('China')
Search('USA') 
    


def SearchTH(kum):
    time.sleep(3)
    for i in range(7):
        pyautogui.press('tab')
    pyautogui.press('backspace')
    pyperclip.copy(kum)
    time.sleep(1)
    pyautogui.click(340,142)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.screenshot(kum + '.png')

SearchTH('ยีนส์')
SearchTH('สวัดดี')

  




