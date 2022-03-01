from helper import menu
from helper import readInt
from helper import readStr
url = 'http://localhost:3333'

menu.dynamicMenu(['Enviar email', 'Sair'], 'MENU PRINCIPAL')

opc = (readInt.readInt('O que deseja fazer: ', 2))

if opc == 1:
    service = readStr.readStr('Serviço de email a ser utilizado: ', 5)
    print(service)
