import pyautogui
import time 
from datetime import datetime
from pynput.mouse import Listener 

sleepTimeInSeconds = 35
totalDurationInseconds = 30 * 60
clicked = False
xCoord = None 
yCoord = None 

def getClickCoord(x,y,pressed):
    global clicked, xCoord, yCoord
    if pressed and not clicked:
        xCoord = x
        yCoord = y
        clicked = True
        return False
    
def runClickCoord():
    print('click t get coordinates \n')
    with Listener(on_click=getClickCoord) as listener:
        listener.join()

def currentTime():
    print('\n')
    return datetime.now().strftime("%H:%M:%S")

def moveAndClick():
    pyautogui.moveTo(xCoord,yCoord)
    pyautogui.click()
    print(f"clicked at X={xCoord}, Y={yCoord}")

def clickCtrl():
    pyautogui.keyDown('ctrl')
    pyautogui.click()
    pyautogui.keyUp('ctrl')
    print('ctrl') 

def cuntdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\r Time remaining for next click : {i} secnds.", end='', flush=True)
        time.sleep(1)

def start():
    for i in range(totalDurationInseconds):
        print(currentTime())
        print(f"count - {i}/{totalDurationInseconds}")
        moveAndClick()
        clickCtrl()
        cuntdown(sleepTimeInSeconds)

def main():
    runClickCoord()
    start()

if __name__ == "__main__":
    main()