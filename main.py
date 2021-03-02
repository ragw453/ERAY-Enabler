import pyautogui
import keyboard


def click():
    pyautogui.typewrite(["esc"])
    pyautogui.click(743,631)
    pyautogui.click(351,179)
    pyautogui.click(451,474)
    pyautogui.click(625,148)
    pyautogui.click(350,49)
    pyautogui.click(815,593)
    pyautogui.click(1486,1004)
    pyautogui.click(1710,1005)
    pyautogui.click(891,876)
    pyautogui.click(822,323)
    pyautogui.typewrite(["esc"])




while True:
    if keyboard.is_pressed("-"):
        click()
    if keyboard.is_pressed("q"):
        quit()