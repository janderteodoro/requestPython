def dynamicMenu(itens, text):
    print('=' * 60)
    print(text.center(60))
    print('=' * 60)

    c = 1 

    for i in itens:
        print(f'[{c}] - {i}')
        c += 1
    
    print()