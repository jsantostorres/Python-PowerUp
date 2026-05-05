import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=670, y=415)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=510, y=375)
pyautogui.write("emaillegal@yahoo.com")
pyautogui.press("tab")
pyautogui.write("Orwell#1984")
pyautogui.press("tab")
pyautogui.press("enter")