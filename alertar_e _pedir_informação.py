# Aletar e pedir informação no pyautogui
import pyautogui
pyautogui.alert(text='Inicializando sua automação', title = 'Automação de Login',button='ok')

# Como pedir informação
email= pyautogui.prompt(text='Digite seu e-mail', title ='Informações obrigatórias')
print(f'Você digitou {email}')

# Confirmar se algo deve ou não acontecer
resposta = pyautogui.confirm(text='Continuar rodando nossa automação?',title='Confirmação',buttons=['sim','não','cancelar'])
if resposta == 'sim':
    print('continuando automação')
elif resposta == 'não':
    print('encerrando automação')
else:
    print('Operação cancelada')


senha = pyautogui.password(text='digite sua senha:',title='dados de login',mask='*')
print('senha')