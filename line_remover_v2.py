import keyboard
import pyperclip
import time

def replaceMultiple(mainString, toBeReplaced, newString):
    # Iterate over the strings to be replaced
    #global modString
    modString = mainString
    for elem in toBeReplaced :
        # Check if string is in the main string
        if elem in modString :
            # Replace the string
            modString = modString.replace(elem, newString)
    
    return modString

while True:
    if keyboard.is_pressed('ctrl+c'):
        time.sleep(0.1)
        mainString = pyperclip.paste()
        modString = ''
        replaceMultiple(mainString,['\r\n'],'')
        replaceMultiple(modString,['◼','&'],' - ')
        pyperclip.copy(modString)    