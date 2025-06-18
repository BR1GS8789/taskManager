from Classes.tasks import *
from time import sleep

from uteis.cabecalho import cabecalho


class Gerenciador:
    def __init__(self):
        self.lista = Tarefas.lista_de_tarefas
    def remover_tarefas(self) -> None:

        if len(self.lista) <= 0:
            print('Não há tarefas.')
        else:
            x = str(input('Insira o título da tarefa para EXCLUIR: '))
            c = 0
            for obj in self.lista:
                if obj.titulo == x:
                    self.lista.remove(obj)
                    print(f'Tarefa "{x}" removida com sucesso.')
                    c = 1
                    break
            if c == 0:
                print('Tarefa não encontrada.')

    def listar_tarefas(self):

        if len(self.lista) == 0:
            cabecalho('Não há tarefas.')
        else:

            c = 1
            cabecalho('Lista de Tarefas')
            sleep(1)
            for obj in self.lista:
                print(f'{c}-   {obj.titulo}')
                print(f'Descrição: {obj.descricao}')
                if obj.prazo > 0:
                    print(f'Prazo: Faltam {obj.prazo} dia(s).')
                elif obj.prazo == 0:
                    print(f'Prazo: HOJE!')
                else:
                    print(f'Prazo: Ultrapassado em {abs(obj.prazo)} dia(s).')
                print(f'Data: {obj.prazofinal.strftime("%d/%m/%Y")}')
                print(f'Status: ',end='')
                if obj.status == False:
                    print('Pendente.')
                else:
                    print('Concluído.')
                c += 1
                print('-'*30)
                sleep(0.5)

    def listar_pendentes(self):
        if len(self.lista) == 0:
            cabecalho('Não há tarefas.')
        else:
            cabecalho('Tarefas pendentes.')
            c = 1
            for obj in self.lista:
                if obj.status == False:
                    print(f'{c}-    {obj.titulo}')
                    if obj.prazo > 0:
                        print(f'Prazo: Faltam {obj.prazo} dia(s).')
                    elif obj.prazo == 0:
                        print(f'Prazo: HOJE!')
                    else:
                        print(f'Prazo: Ultrapassado em {abs(obj.prazo)} dia(s).')
                    if c > 1:
                        print('-'*30)
                    c += 1
                    sleep(0.5)

    def buscar_tarefa(self):
        if len(self.lista) == 0:
            cabecalho('Não há tarefas.')
        else:
            try:
                a = str(input('Digite o título da tarefa: '))
            except:
                print('\033[031mErro! Digite um título válido!\033[m')
                a = str(input('Digite o título da tarefa: '))
            while a == '':
                print('\033[031mErro! Digite um título válido!\033[m')
                a = str(input('Digite o título da tarefa: '))
            c = 1

            encontrado = False

            for obj in self.lista:

                if obj.titulo == a:
                    print(f'{c}-    {obj.titulo}')
                    print(f'Descrição: {obj.descricao}')
                    if obj.prazo > 0:
                        print(f'Prazo: Faltam {obj.prazo} dia(s).')
                    elif obj.prazo == 0:
                        print(f'Prazo: HOJE!')
                    else:
                        print(f'Prazo: Ultrapassado em {abs(obj.prazo)} dia(s).')
                    print(f'Data: {obj.prazofinal.strftime("%d/%m/%Y")}')
                    print(f'Status: ', end='')
                    if obj.status == False:
                        print('Pendente.')
                    else:
                        print('Concluído.')
                        print('-' * 30)
                        sleep(0.5)
                    c += 1
                    encontrado = True

            if encontrado == False:

                print('Tarefa não encontrada.')

    def ordenar_prazo(self):

        if len(self.lista) == 0:
            cabecalho('Não há tarefas.')
        else:
            lista_ordenada = sorted(self.lista, key=lambda tarefa: tarefa.prazo)
            c = 1
            for obj in lista_ordenada:
                print(f'{c}-    {obj.titulo}')
                print(f'Descrição: {obj.descricao}')
                if obj.prazo > 0:
                    print(f'Prazo: Faltam {obj.prazo} dia(s).')
                elif obj.prazo == 0:
                    print(f'Prazo: HOJE!')
                else:
                    print(f'Prazo: Ultrapassado em {obj.prazo * obj.prazo} dia(s).')
                print('-'*30)
                sleep(0.5)
                c += 1

    def concluir_tarefa(self):

        if len(self.lista) <= 0:
            cabecalho('Não há tarefas.')
        else:
            x = str(input('Insira o título da tarefa para CONCLUIR: '))
            c = 0
            for obj in self.lista:
                if obj.titulo == x:
                    obj.status = True
                    print(f'Tarefa "{x}" concluída com sucesso.')
                    c = 1
                    break
            if c == 0:
                print('Tarefa não encontrada.')
