from helper import Helper, Payload
from service.sendEmail import sendMail
import sys


if __name__ == '__main__':
    try:
        url = 'http://localhost:3333'
        Helper.dynamicMenu(['Enviar email', 'Sair'], 'MENU PRINCIPAL')
        opc = (Helper.readInt('O que deseja fazer: ', 2))
        if opc == 1:
            payload = Payload.makePayload()
            sendMail(f'{url}/sendMail', payload)
        else:
            sys.exit()
    except:
        print(f'Erro ao executar app')