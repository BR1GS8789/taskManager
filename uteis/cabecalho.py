def cabecalho(texto):
    print('-' * (30 if len(texto) < 30 else 60))
    print(f'{texto:^30}')
    print('-' * (30 if len(texto) < 30 else 60))