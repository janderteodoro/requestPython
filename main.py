from helper.menu import dynamicMenu
from helper.readInt import readInt
from helper.makePayload import makePayload
from service.sendEmail import sendMail

url = 'http://localhost:3333'

dynamicMenu(['Enviar email', 'Sair'], 'MENU PRINCIPAL')

opc = (readInt('O que deseja fazer: ', 2))

if opc == 1:
    payload = makePayload()
    sendMail(f'{url}/sendMail', payload)