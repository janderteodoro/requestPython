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