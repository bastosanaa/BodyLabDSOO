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
        if values['0'] or button in(None, "Cancelar"):
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
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistma BodyLab').Layout(layout)
    
    def pega_dados_matricula(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("----------- Realizar Matricula ------------", font=('Fira Code', 25))],
            [sg.Text('Insira o nome do aluno: ', size=(15,1)), sg.InputText('', key='aluno')],
            [sg.Text('Numero de Telefone: ', size=(15,1)), sg.InputText('', key='numero_telefone')],
            [sg.Text('E-mail: ', size=(15,1)), sg.InputText('', key='email')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Matricula').Layout(layout)
    
        button, values = self.open()
        aluno = values['aluno']
        numero_telefone = values['numero_telefone'] 
        email = values['email']

        self.close()
        return {"aluno": aluno, "numero_telefone": numero_telefone, "email": email}

    def pega_dados_matricula(self, turno, plano):
        layout = [
            [sg.Text("----------- Realizar matrícula ------------")],
            [sg.Text('Insira o nome do aluno: '), sg.InputText('', key='aluno')],
            [sg.Text('Selecione o turno:'), sg.Combo(self.__turnos, key='turno')],
            [sg.Text('Selecione o plano:'), sg.Combo(self.__planos, key='plano')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        
        self.__window = sg.Window('Matrícula').Layout(layout)
        button, values = self.open()
    
        aluno = values['aluno']
        turno = values['turno']
        plano = values['plano']

        self.close()
        return {"aluno": aluno, "turno": turno, "plano": plano}

        
    def seleciona_id_matricula(self):
        layout = [
            [sg.Text('Insira o id da matrícula: '), sg.InputText('', key='id_matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        
        self.__window = sg.Window('Matrícula').Layout(layout)
        button, values = self.open()
    
        id_matricula = int(values['id_matricula'])
        
        self.close()
        return {'id_matricula': id_matricula}


    def mostra_dados_matricula(self, dados_matricula):
        layout = [
            [sg.Text("-------- Dados da Matrícula ----------")],
            [sg.Text(f"ID: {dados_matricula['id_matricula']}")],
            [sg.Text(f"Aluno: {dados_matricula['aluno']}")],
            [sg.Text(f"Turno: {dados_matricula['turno']}")],
            [sg.Text(f"Plano: {dados_matricula['plano']}")],
            [sg.Text(f"Mensalidade: {dados_matricula['mensalidade']}")],
            [sg.Text(f"Data de Início: {dados_matricula['data_inicio_matricula']}")],
            [sg.Text(f"Data de Vencimento: {dados_matricula['data_vencimento_matricula']}")],
            [sg.Text(f"Data de Término: {dados_matricula['data_termino_matricula']}")],
            [sg.Button('OK')]
        ]
        window = sg.Window('Dados da Matrícula', layout)
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, 'OK'):
                break
        window.close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
    
    def relatorios(self, resultado):
        print(resultado)

    def mostra_mensagem(self, msg):

        print(msg)