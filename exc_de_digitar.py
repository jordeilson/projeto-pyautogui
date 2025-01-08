'''Crie um programa que vai até onde seu bloco de notas
estiver aberto e digita a frase
"Automação é Incrivel'''
import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')
# mover o mouse até o campo digitado
pyautogui.moveTo(1039,120,duration=2)
# Clicar no campo digitado
pyautogui.doubleClick()
# Digitar minha mensagem
escrever_frase('Automação é Incrível')
'''pyautogui.typewrite('Automação é Incrível')'''