from helper import menu
from helper import readInt

menu.dynamicMenu(['Enviar email', 'Sair'], 'MENU PRINCIPAL')
opc = (readInt.readInt('O que deseja fazer: ', 2))

url = 'http://localhost:3333'

