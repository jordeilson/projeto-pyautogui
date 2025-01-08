# Como usar a função click
import pyautogui
# Click personalizado
pyautogui.click(x =1019,y = 385, clicks=2,interval= 1, button= 'left', duration=2) # left = esquerda, "botão esquerdo do mouse"

# Click na posição atual ( Com o botão esquerdo) 
pyautogui.click()
pyautogui.click(button = 'left') # Botão esquerdo
pyautogui.click(button = 'right') # Botão direito
pyautogui.click(button = 'middle') # Botão do meio

# Clicar x Vezes
pyautogui.click(clicks = 10)

# Funções prontas para clicks
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.tripleClick()

