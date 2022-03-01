from helper import menu
from helper import readInt
from helper import readStr
import json

url = 'http://localhost:3333'

menu.dynamicMenu(['Enviar email', 'Sair'], 'MENU PRINCIPAL')

opc = (readInt.readInt('O que deseja fazer: ', 2))

if opc == 1:
    service = readStr.readStr('Serviço de email a ser utilizado: ', 5)
    print()
    user = readStr.readStr(f'Nome de usuário (@{service}.com): ', 8)
    print()
    password = readStr.readStr(f'Senha para {user}: ', 5)
    print()
    receiver = readStr.readStr('Para quem vai enviar esse email? ', 8)
    print()
    subject = readStr.readStr('Assunto do email: ', 4)
    print()
    textEmai = readStr.readStr(f'Escreva seu Email: \n\n', 10)

    payload = {
        "service": service,
        "auth": {
            "user": user, 
            "pass": password
        }, 
        "mailOptions": {
            "from": user, 
            "to": receiver, 
            "subject": subject, 
            "text": textEmai
        }
    }

    payload = json.dumps(payload, indent=4, sort_keys=True)

    print(payload)
