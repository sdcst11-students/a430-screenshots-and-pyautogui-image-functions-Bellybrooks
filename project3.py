import pyautogui
import time
def task1():
    pyautogui.moveTo(432,529)
    pyautogui.mouseDown(432,529)
    time.sleep(5)
    pyautogui.mouseUp()
    time.sleep(.2)

def task2():
    pyautogui.moveTo(768,545)
    pyautogui.mouseDown(768,545)
    time.sleep(7)
    pyautogui.mouseUp()
    time.sleep(.2)

def task3():
    try:
        loco = pyautogui.locateCenterOnScreen('assets/upss2.png', confidence=0.7)
        x=loco.x
        y=loco.y + 100
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        y= y + 100
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        y= y + 100
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        
    except:
        print('fail')

def task4():
    try:
        pyautogui.locateCenterOnScreen('assets/workbut.png', confidence=0.7)
        return False
    except:
        return True





if __name__ == "__main__":
    x = pyautogui.alert('https://asdehielo.itch.io/push-the-square')
    while True:
        task1()
        task2()
        task3()
        if task4():
            exit()