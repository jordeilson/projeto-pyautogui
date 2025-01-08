# Como usar botões de atalho do teclado
import pyautogui

# Como usar combinações de teclas
pyautogui.click(1503,234,duration=2)
# Simular "Segurar uma tecla"
pyautogui.keyDown('ctrl')
pyautogui.keyDown('a')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('a')

# Como usar botões e atalhos de teclado
import pyautogui

# Como usar combinações de teclas
pyautogui.click(1503,234,duration=2)
# Simular "Segurar de uma teclas"
pyautogui.hotkey('crtl','a')
pyautogui.click('1468,516,duration=2')
pyautogui.hotkey('ctrl','v')