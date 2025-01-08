# Crie um programa que pede ao usuário email ea senha e, na sequência, copia e cola
# o usuário e senha de um bloco de notas

import pyautogui


email = pyautogui.prompt(text='Digite seu email:', title='Informações obrigatórias')
senha = pyautogui.password(text='Digite sua senha:',title='dados de login',mask='*')

pyautogui.click(1322,240,duration=2)
pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)
pyautogui.press('enter')