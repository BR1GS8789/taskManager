from Classes.tasks import Tarefas
from Classes.gerenciador import Gerenciador
from uteis.cabecalho import cabecalho
from uteis.validadorint import leiaInt
from time import sleep
def CriarTarefa() -> None:

    a = Tarefas()
    print('Tarefa criada com sucesso!')
def opcs():
    cabecalho('Menu De Opções')
    print('''    1. Criar Tarefa
    2. Listar Tarefas
    3. Listar Pendentes
    4. Listar por Prazo
    5. Concluir Tarefa
    6. Remover Tarefas
    7. Buscar Tarefas Por Título
    8. Fechar Sistema''')
    print('-' * 30)

def menu() -> None:
    x = Gerenciador()
    while True:
        opcs()
        a = leiaInt('Sua Opção: ',initial=1, end=8)
        if a == 1: # Criar Tarefas
            CriarTarefa()
            sleep(2)

        elif a == 2: # Listar Tarefas
            x.listar_tarefas()
            sleep(2)

        elif a == 3: # Listar Tarefas Pendentes
            x.listar_pendentes()
            sleep(2)

        elif a == 4: # Listar Por Prazo
            x.ordenar_prazo()
            sleep(2)

        elif a == 5: # Concluir Tarefa
            x.concluir_tarefa()
            sleep(2)

        elif a == 6: # Remover Tarefa
            x.remover_tarefas()
            sleep(2)

        elif a == 7: # Buscar por título
            x.buscar_tarefa()
            sleep(2)

        elif a == 8: # Fechar o sistema

            cabecalho('Volte sempre')
            sleep(1)
            break