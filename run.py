import time
import pyautogui
import pandas as pd

pyautogui.PAUSE = 0.8

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

URL = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(URL)
pyautogui.press('enter')

time.sleep(3)

pyautogui.click(x=935, y=470)
pyautogui.write('admin@gmail.com')

pyautogui.press('tab')
pyautogui.write('password')

pyautogui.click(x=935, y=696)
time.sleep(3)

table = pd.read_csv('products.csv')

for line in table.index:
    pyautogui.click(x=933, y=325)
    for column in table.columns:
        if not pd.isna(table.loc[line, column]):
            pyautogui.write(str(table.loc[line, column]))
        pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)
