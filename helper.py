import json
from getpass import getpass

class Helper:

    #method to make menu
    def dynamicMenu(itens, text):
        print('=' * 60)
        print(text.center(60))
        print('=' * 60)

        c = 1 

        for i in itens:
            print(f'[{c}] - {i}')
            c += 1
        
        print()

    #method to read int numbers
    def readInt(txt, itensAmount):
        while True:
            try:
                n = int(input(txt))
            except(TypeError, ValueError):
                print('Insira números por favor')
                continue
            else:
                if ( n < 1 ) or ( n > itensAmount ):
                    print('Opção Inválida. Tente Novamente')
                    continue
                else:
                    return n


    #methods to read string 
    def readStr(txt, size):
        while True:
            try:
                word = str(input(txt).strip())
            except(TypeError, ValueError):
                print('Insira números por favor')
                continue
            else:
                if len(word) < size:
                    print(f'Necessário pelo menos {size} letras')
                    continue
                else:
                    return word


class Payload():
        
    #method to built payload who goes realize request in API 
    def makePayload():
        service = Helper.readStr('Serviço de email a ser utilizado: ', 5)
        print()
        user = Helper.readStr(f'Nome de usuário (@{service}.com): ', 8)
        print()
        password = getpass(f'Senha para {user}: ')
        print()
        receiver = Helper.readStr('Para quem vai enviar esse email? ', 8)
        print()
        subject = Helper.readStr('Assunto do email: ', 4)
        print()
        textEmai = Helper.readStr(f'Escreva seu Email: \n\n', 10)

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

        return payload
