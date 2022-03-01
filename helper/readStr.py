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

