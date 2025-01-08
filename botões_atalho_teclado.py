# Como usar botões e atalhos do teclado
import pyautogui
from time import sleep

# Navegar e clicar no campo email
pyautogui.click(1411,265,duration=2)
sleep(1)
# Digitar o email
pyautogui.typewrite('admin#hotmail.com')
sleep(1)
# Apertar TAB
pyautogui.press('tab')
sleep(1)
# Digitar minha senha
pyautogui.typewrite('123456')
sleep(1)
# Apertar TAB
pyautogui.press('tab')
# Apertar space
pyautogui.press('space')
er