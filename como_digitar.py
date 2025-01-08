# Como digitar com o pyautogui
import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')


# Mover o mouse até o campo de digitar
pyautogui.moveTo(1585,1009,duration=2)
# Clicar no campo de digitar
pyautogui.click()
# Digitar minha mensagem
escrever_frase('Olá, Bom dia!')
'''Pyautogui.typewrite('Olá, bom dia!)'''  # nesse caso melhor fazer uma função, pq ele não vai imprimir as palavras com acento
# Cliciar no botão de enviar
pyautogui.click(1880,1003,duration=2)

''' Como usar os botões de atalho do teclado'''
import pyautogui

# para ver todas possíveis teclas, rode:
print(pyautogui.KEYBOARD_KEYS)
