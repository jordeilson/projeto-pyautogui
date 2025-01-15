'''DESAFIO 🥇
1) Navegue até o site https://cursoautomacao.netlify.app/
2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
3) Clique em alerta, para gerar a alerta
4) Feche a alerta
5) Suba a página totalmente para cima
6) Desça apenas o suficiente para conseguir chegar até a seção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"'''
import pyautogui
import pyperclip
from time import sleep

pyautogui.moveTo(1067,284,duration=2)
pyautogui.scroll(-2100)
pyautogui.click(785,321,duration=2)

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

escrever_frase('Jordeilson Silva Lima')
pyautogui.click(794,357,duration=1)
pyautogui.doubleClick(1206,175,duration=1)
sleep(1)
pyautogui.scroll(2100)
sleep(1)
pyautogui.scroll(-3300)
sleep(1)
pyautogui.click(844,227,duration=2)
sleep(1)
pyautogui.click(879,331,duration=2)
sleep(1)
pyautogui.alert(text='vOCÊ TERMINOU!!!',title='Acabou',button='OK')
