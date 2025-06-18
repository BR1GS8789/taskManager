def leiaInt(msg='Digite um número inteiro: ', r='ERRO! Digite uma opção válida.',initial=0, end=1000):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0:31m{r}\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0:31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        if n < initial or n > end:
            print(f'\033[0:31m{r}\033[m')
            continue
        else:
            return n
