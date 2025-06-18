def continuar(text='Deseja continuar? [S/N] ', msg='ERRO! Digite apenas S ou N.'):
    while True:
        a = str(input(text)).strip().upper()[0]
        while a[0] != 'S' and a[0] != 'N':
            print(f'\033[31m{msg}\033[m')
            a = str(input(text)).strip().upper()[0]
        if a == 'N':
            return False
        else:
            return True
