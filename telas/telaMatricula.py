from telas.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg
import json


class TelaMatricula(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_opcoes()
        self.__turnos = ['Matutino', 'Vespertino', 'Noturno']
        self.__planos = ['Silver', 'Gold', 'Diamond']

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        if values['0'] or button in (None, "Cancelar"):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("Matriculas", font=('Helvetica', 25, 'bold'))],
            [sg.Radio('Realizar Matrícula', "RD1", key='1')],
            [sg.Radio('Cancelar Matrícula', "RD1", key='2')],
            [sg.Radio('Listar Matrículas', "RD1", key='3')],
            [sg.Radio('Vizualizar Matricula Específica', "RD1", key='4')],
            [sg.Radio('Alterar Plano', "RD1", key='5')],
            [sg.Radio('Alterar Turno', "RD1", key='6')],
            [sg.Radio('Plano mais procurado', "RD1", key='7')],
            [sg.Radio('Turno mais procurado', "RD1", key='8')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistma BodyLab').Layout(layout)

    def pega_dados_matricula(self, turno, plano):
        sg.theme('DarkPurple1')
        layout = [
            [sg.Text("Realizar Matricula", font=('Helvetica', 25, 'bold'))],
            [sg.Text('Insira o nome do aluno: ', font=('Helvetica', 12)), sg.InputText('', key='aluno')],
            [sg.Text('Selecione o turno:', font=('Helvetica', 12)), sg.Combo(self.__turnos, key='turno'), sg.Text('Selecione o plano:', font=('Helvetica', 12)), sg.Combo(self.__planos, key='plano')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistema BodyLab').Layout(layout)
        button, values = self.open()

        aluno = values['aluno']
        turno = values['turno']
        plano = values['plano']

        self.close()
        self.init_opcoes()
        return {"aluno": aluno, "turno": turno, "plano": plano}

    def seleciona_id_matricula(self):
        layout = [
            [sg.Text('Insira o id da matrícula: ', font=('Helvetica', 15, 'bold'))],
            [sg.InputText('', key='id_matricula')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]

        self.__window = sg.Window('Sistema BodyLab').Layout(layout)
        button, values = self.open()

        id_matricula = int(values['id_matricula'])

        self.close()
        return id_matricula


    def lista_de_matricula(self, dados_matriculas):
        lista_matriculas = [[
            id_matricula,
            dados["aluno"],
            dados["turno"],
            dados["plano"],
            dados["mensalidade"],
            dados["data_inicio_matricula"],
            dados["data_vencimento_matricula"],
            dados["data_termino_matricula"]
        ] for id_matricula, dados in dados_matriculas.items()]

        headers = ["ID", "Aluno", "Turno", "Plano", "Mensalidade", "Data de Início", "Data de Vencimento",
                   "Data de Término"]

        layout = [
            [sg.Column([[sg.Text('Matriculas Cadastradas', justification='center', font=('Helvetica', 20, 'bold'))]],
                       expand_x=True)],
            [sg.Table(values=lista_matriculas, headings=headers, display_row_numbers=False, auto_size_columns=True,
                      num_rows=min(25, len(lista_matriculas)))],
            [sg.Button('OK', button_color=('white', 'green'))]
        ]

        self.__window = sg.Window('Sistema BodyLab').Layout(layout)

        button, values = self.open()
        self.close()

    def mostra_matricula(self, dados_matricula):
        layout = [
            [sg.Text('DADOS DA MATRICULA', font=("Helvetica", 15, 'bold'))],
            [sg.Text("ID: ", font=("Helvetica", 10, 'bold')), sg.Text(str(dados_matricula["id_matricula"]))],
            [sg.Text("Aluno: ", font=("Helvetica", 10, 'bold')), sg.Text(dados_matricula["aluno"])],
            [sg.Text("Turno: ", font=("Helvetica", 10, 'bold')), sg.Text(dados_matricula["turno"])],
            [sg.Text("Plano: ", font=("Helvetica", 10, 'bold')), sg.Text(dados_matricula["plano"])],
            [sg.Text("Mensalidade: ", font=("Helvetica", 10, 'bold')), sg.Text(str(dados_matricula["mensalidade"]))],
            [sg.Text("Data de Início: ", font=("Helvetica", 10, 'bold')),
             sg.Text(str(dados_matricula["data_inicio_matricula"]))],
            [sg.Text("Data de Vencimento: ", font=("Helvetica", 10, 'bold')),
             sg.Text(str(dados_matricula["data_vencimento_matricula"]))],
            [sg.Text("Data de Término: ", font=("Helvetica", 10, 'bold')),
             sg.Text(str(dados_matricula["data_termino_matricula"]))],
            [sg.Button('OK', button_color=('white', 'green'))]
        ]

        self.__window = sg.Window('DADOS DA MATRICULA', layout)

        button, values = self.open()

        self.close()

    def pega_dados_plano(self):
        layout = [
            [sg.Text('Selecione o plano:', font=('Helvetica', 15, 'bold')), sg.Combo(self.__planos, key='plano')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]

        self.__window = sg.Window('Selecionar Plano').Layout(layout)
        button, values = self.open()

        plano = values['plano']

        self.close()
        return plano

    def pega_dados_turno(self):
        layout = [
            [sg.Text('Selecione o turno:'), sg.Combo(self.__turnos, key='turno')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]

        self.__window = sg.Window('Sistema BodyLab').Layout(layout)
        button, values = self.open()

        turno = values['turno']

        self.close()
        return turno

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def relatorios(self, resultado):
        layout = [
            [sg.Text(resultado, font=('Helvetica', 15, 'bold'))],
            [sg.Button('OK')]
        ]

        self.__window = sg.Window('Sistema Bodylab', layout)

        while True:
            event, values = self.__window.read()
            if event in (sg.WINDOW_CLOSED, 'OK'):
                break

        self.__window.close()
        self.__window = None

    def mostra_mensagem(self, msg):
        layout = [
            [sg.Text(msg, font=('Helvetica', 15, 'bold'))],
            [sg.Button('OK')]
        ]

        self.__window = sg.Window('Sistema BodyLab', layout)

        while True:
            event, values = self.__window.read()
            if event in (sg.WINDOW_CLOSED, 'OK'):
                break

        self.__window.close()
