"""
from python_imagesearch.imagesearch import imagesearch

pos = imagesearch("AuctionSearch.png")
if pos[0] != -1:
    print("Se encontro la imagen")
else:
    print("image not found")

"""


from pynput.keyboard import Key, Controller
from pynput import keyboard
import pyautogui
import msvcrt
import time

keyPress = Controller()

break_program = False
def on_press(key):
    global break_program
    if key == keyboard.Key.end:
        print ('end pressed')
        break_program = True
        return False
    
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if k == "q":
        print("bot invoked")
        while True:
            pyautogui.press("enter")
            time.sleep(0.4)
            pyautogui.press("enter")
            time.sleep(1)

        # Si encuentra subasta
            pyautogui.press("y")
            time.sleep(0.1)
            pyautogui.press("down")
            time.sleep(0.5)
            pyautogui.press("enter")
            time.sleep(0.1)
            pyautogui.press("enter")
            time.sleep(0.1)

        # Si no la encuentra
            pyautogui.press("esc")
            time.sleep(1)
            print("cicle complete")
            
        

with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False:
        print ('program running')
        time.sleep(15)
    listener.join()