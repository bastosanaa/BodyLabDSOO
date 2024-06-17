import PySimpleGUI as sg
from telas.telaAbstrata import TelaAbstrata



class TelaFicha(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()

        lista_opcoes  = {
        "0" : 0,
        "1" : 1,
        "2" : 2,
        "3" : 3,
        }

        if button in (None, "Cancelar"):
            opcao = 0
            self.close()
            return opcao
        for key, value in values.items():
            if value:  # Se o valor for True
                opcao = lista_opcoes[key]
                break
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("Fichas", font=('Helvetica', 25))],
            [sg.Radio('Criar Ficha', "RD1", key='1')],
            [sg.Radio('Remover Ficha', "RD1", key='2')],
            [sg.Radio('Listar Fichas', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar',button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistma BodyLab').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, msg):
        layout = [
            [sg.Text(msg)],
            [sg.Button('OK')]
        ]

        self.__window = sg.Window('Mensagem', layout)

        while True:
            event, values = self.__window.read()
            if event in (sg.WINDOW_CLOSED, 'OK'):
                break

        self.__window.close()

    def pega_dados_nova_ficha(self):
        sg.ChangeLookAndFeel('DarkPurple1')

        numero_treinos = [1,2,3,4,5]

        layout = [
            [sg.Text("Criar Ficha", font=('Helvetica', 25, 'bold'), justification='center')],
            [sg.Text('Descrição: ', )],
            [sg.InputText('', key='descricao')],
            [sg.Text('Numero de Treinos: ', )],
            [sg.Combo(numero_treinos, key='numero_treinos', readonly=True)],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Button('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistema BodyLab', layout)

        button, values = self.open()
        self.close()

        if button == 'Confirmar':
            descricao = values['descricao']
            numero_treinos = values['numero_treinos']

            return {
                'descricao': descricao,
                'numero_treinos': numero_treinos,
            }

    def pega_dados_treino(self):
        layout = [
            [sg.Text("Criar Treino", font=('Helvetica', 25, 'bold'), justification='center')],
            [sg.Text('Titulo: ', )],
            [sg.InputText('', key='titulo')],
            [sg.Text('exercicio 1: ', )],
            [sg.InputText('', key='exercicio_1')],
            [sg.Text('exercicio 2: ', )],
            [sg.InputText('', key='exercicio_2')],
            [sg.Text('exercicio 3: ', )],
            [sg.InputText('', key='exercicio_3')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Button('Cancelar', button_color=('white', 'red'))]
        ]
        
        self.__window = sg.Window('Sistema BodyLab', layout)

        button, values = self.open()
        self.close()

        if button == 'Confirmar':
            titulo = values['titulo']
            exercicio_1 = values['exercicio_1']
            exercicio_2 = values['exercicio_2']
            exercicio_3 = values['exercicio_3']

            return {
                'titulo' : titulo,
                'exercicio_1' : exercicio_1,
                'exercicio_2' : exercicio_2,
                'exercicio_3' :exercicio_3
            }