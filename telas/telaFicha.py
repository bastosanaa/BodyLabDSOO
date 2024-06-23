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

        #verificacao da descricao

        if button == 'Confirmar':
            descricao = values['descricao']
            numero_treinos = values['numero_treinos']

            if self.verifica_se_string(descricao):
                return {
                    'descricao': descricao,
                    'numero_treinos': numero_treinos,
                }
            self.mostra_mensagem("Tente Novamente. Descrição inválida")
            return None

    def verifica_se_string(self, entrada):
        entrada.replace('', ',')
        if entrada.isalpha():
            return True
        return None

    def pega_dados_treino(self):

        treinos = [
            "quadriceps",
            "glúteos",
            "posteriores",
            "costas",
            "braço",
            "peito"
        ]

        layout = [
            [sg.Text("Criar Treino", font=('Helvetica', 25, 'bold'), justification='center')],
            [sg.Text('Treino: ')],
            [sg.Combo(treinos, key='treino', readonly=True)],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Button('Cancelar', button_color=('white', 'red'))]
        ]
        
        self.__window = sg.Window('Sistema BodyLab', layout)

        button, values = self.open()
        self.close()

        if button == 'Confirmar':
            treino = values['treino']

            if treino:

                return {
                    "treino": treino
                }
            else:
                self.mostra_mensagem("Por favor preencha todos os campos")
            
    def mostra_ficha(self, dados_ficha, numero_ficha, total_fichas):
        sg.ChangeLookAndFeel('DarkPurple1')

        layout = [
        [sg.Text(f'Ficha {numero_ficha}/{total_fichas}', font=('Helvetica', 25, 'bold'), justification='center')],
        [sg.Text(f"ID: {dados_ficha['id_ficha']}")],
        [sg.Text(f"Descrição: {dados_ficha['descricao']}")],
        [sg.Text(f"Número de trienos: {dados_ficha['numero_treinos']}")],
        [sg.Text(f"Treinos: {dados_ficha['treinos']}")],
        [sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]

        self.__window = sg.Window('Sistema BodyLab').Layout(layout)

        while True:
            event, values = self.__window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break

        self.__window.close()

    def pega_dados_remover_ficha(self):
            sg.ChangeLookAndFeel('DarkPurple1')

            layout = [
            [sg.Text("insira o ID da ficha a ser removida", font=('Helvetica', 25, 'bold'), justification='center')],
            [sg.Text('ID: ', )],
            [sg.InputText('', key='id_ficha')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Button('Cancelar', button_color=('white', 'red'))]
            ]

            self.__window = sg.Window('Sistema BodyLab', layout)

            button, values = self.open()
            self.close()

            if button == 'Confirmar':
                id_ficha = values['id_ficha']

            try:
                id_ficha = int(id_ficha)
                return {
                    "id_ficha": id_ficha,
                }
            except ValueError:
                self.mostra_mensagem('Tente novamente. ID inválido.')
            


            