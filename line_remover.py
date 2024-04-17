import keyboard
import pyperclip
import time
import re

while True:
    if keyboard.is_pressed('ctrl+c'):
        time.sleep(0.1)
        texttomod = pyperclip.paste()
        modtext = texttomod.replace('\r\n','')
        modtext = modtext.replace('•','\n')
        #modtext = modtext.replace('-','')
        modtext = re.sub(r'\-(?!\d)', '', modtext) #match dash if not followed by number
        pyperclip.copy(modtext)        