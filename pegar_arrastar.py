# Como pegar e "arrastar" algo para outro lugar.
import pyautogui
for i in range(10):
    #  Mover até uma coordenada.
    pyautogui.moveTo(1358,257,duration=0.5)
    #clicar arrastaraté ium ponto e soltar
    pyautogui.dragTo(1360,790,button='left',duration=0.5)
    #repetir 9 vezes