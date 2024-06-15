from telas.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg


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
            [sg.Text("Matriculas", font=('Fira Code', 25))],
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
            [sg.Text('Insira o nome do aluno: '), sg.InputText('', key='aluno')],
            [sg.Text('Selecione o turno:'), sg.Combo(self.__turnos, key='turno'), sg.Text('Selecione o plano:'), sg.Combo(self.__planos, key='plano')],
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

    def gerar_string_matricula(self, dados_matricula):
        string_matricula = ''
        string_matricula += "ID: " + str(dados_matricula["id_matricula"]) + '\n'
        string_matricula += "Aluno: " + dados_matricula["aluno"] + '\n'
        string_matricula += "Turno: " + dados_matricula["turno"] + '\n'
        string_matricula += "Plano: " + dados_matricula["plano"] + '\n'
        string_matricula += "Mensalidade: " + str(dados_matricula["mensalidade"]) + '\n'
        string_matricula += "Data de Início: " + str(dados_matricula["data_inicio_matricula"]) + '\n'
        string_matricula += "Data de Vencimento: " + str(dados_matricula["data_vencimento_matricula"]) + '\n'
        string_matricula += "Data de Término: " + str(dados_matricula["data_termino_matricula"]) + '\n'
        return string_matricula

    def lista_de_matricula(self, dados_matricula):
        string_matricula = self.gerar_string_matricula(dados_matricula)
        layout = [
            [sg.Text('LISTA DE MATRICULAS', font=('Helvetica', 15, 'bold'))],
            [sg.Text(string_matricula)],
            [sg.Button('OK', button_color=('white', 'green'))]
        ]
        self.__window = sg.Window('Sistema BodyLab').Layout(layout)

        button, values = self.open()
        self.close()

    def mostra_matricula(self, dados_matricula):
        string_matricula = self.gerar_string_matricula(dados_matricula)
        sg.Popup('MATRICULA', string_matricula)

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
