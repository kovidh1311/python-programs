import random
import pyautogui
import time
pyautogui.click(1150,1050,duration=2)
a = 10
while  a == 10 :
    q = random.randint (1,6)
    pyautogui.click(1400,850,duration=2)
    if q == 1 :
     pyautogui.typewrite('trade pls')  
    elif q == 2 :
     pyautogui.typewrite('im big fan')
    elif q == 3 :
     pyautogui.typewrite('i need shadow')
    elif q == 4 :
     pyautogui.typewrite('!points')
    elif q == 5 :
     pyautogui.typewrite('trading blizzard') 
    elif q == 6 :
     pyautogui.typewrite('who has buddha')  
    pyautogui.click(1700,850,duration=2)
    time.sleep(40)