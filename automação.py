# Crie um desafio que navega até o site
# ​https://pt.wikipedia.org/wiki/Brasil e desce a página o suficiente
# para chegar na seção de "historia"

import pyautogui
from time import sleep
pyautogui.moveTo(933,663,duration=2)
pyautogui.click()
sleep(2)
pyautogui.scroll(-4300)