import pyautogui
import time

def wait(seconds):
    time.sleep(seconds)
if __name__=="__main__":
    pyautogui.hotkey("winleft")
    wait(2)
    pyautogui.write("calculator")
    wait(2)
    pyautogui.press("enter")
    wait(2)
    pyautogui.write("3")
    wait(2)
    pyautogui.press("+")
    wait(2)
    pyautogui.write("2")
    wait(2)
    pyautogui.press("enter")