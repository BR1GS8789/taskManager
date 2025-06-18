from calendar import month
from datetime import date, datetime
from uteis.validador import continuar
class Tarefas:
    lista_de_tarefas = []
    def __init__(self):

        self.hoje = date.today()
        self.titulo = str(input('Título da Tarefa: ')).capitalize()
        self.descricao = str(input('Descrição da Tarefa: ')).capitalize()
        self.prazofinal = self.definir_prazo()
        self.status = continuar('Marcar tarefa como concluída? [S/N] ')
        self.prazo = self.diasfaltantes.days
        Tarefas.lista_de_tarefas.append(self)

    def definir_prazo(self):

        hoje = date.today()
        while True:
            try:
                prazo = date(
                day=int(input('Dia: ')),
                month = int(input('Mês: ')),
                year = int(input('Ano: ')))
                if prazo < hoje:
                    print('O prazo não pode ser anterior à data de hoje ')
                    continue
                else:
                    break
            except:
                print('Data inválida! Insira uma data válida.')
        self.diasfaltantes = prazo - self.hoje
        return prazo