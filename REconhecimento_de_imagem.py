# Reconhecimento de imagem simples com pyautogui
import pyautogui
'''
# encontrar as coordenadas próximas de onde aquela imagem está
print(pyautogui.locateOnScreen('numero_4.png'))
# encontrar a coordenada do centro de uma imagem
print(pyautogui.locateCenterOnScreen('numero_4.png'))
#como usar na prática:
pyautogui.click(964,468,445,926,duration=2)
'''
captcha=pyautogui.locateCenterOnScreen('google4.png')
pyautogui.click(captcha[0], captcha[1],duration=2)
