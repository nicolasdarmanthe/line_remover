import keyboard
import pyperclip
import time

while True:
    if keyboard.is_pressed('ctrl+c'):
        time.sleep(0.1)
        texttomod = pyperclip.paste()
        modtext = texttomod.replace('\r\n','')
        pyperclip.copy(modtext)        