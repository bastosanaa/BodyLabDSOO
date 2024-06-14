import PySimpleGUI as sg

from telas.telaAbstrata import TelaAbstrata

class TelaAluno(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3   
        if values['0'] or button in(None, "Cancelar"):
            opcao = 0
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("Aluno", font=('Fira Code', 25))],
            [sg.Radio('Cadastrar Aluno', "RD1", key='1')],
            [sg.Radio('Remover Aluno', "RD1", key='2')],
            [sg.Radio('Listar Alunos', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistma BodyLab').Layout(layout)
    
    def pega_dados_aluno(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("----------- Cadastrar Aluno ------------", font=('Fira Code', 25))],
            [sg.Text('Nome: ', size=(15,1)), sg.InputText('', key='nome')],
            [sg.Text('Numero de Telefone: ', size=(15,1)), sg.InputText('', key='numero_telefone')],
            [sg.Text('E-mail: ', size=(15,1)), sg.InputText('', key='email')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistma BodyLab').Layout(layout)
    
        button, values = self.open()
        nome = values['nome']
        numero_telefone = values['numero_telefone'] 
        email = values['email']

        self.close()
        return {"nome": nome, "numero_telefone": numero_telefone, "email": email}

    def mostra_aluno(self, dados_aluno):
        string_todos_alunos = ""
        for dado in dados_aluno:
            string_todos_alunos = string_todos_alunos + "Nome: " + dado["nome"] + '\n'
            string_todos_alunos = string_todos_alunos + "Telefone: " + str(dado["numero_telefone"]) + '\n'
            string_todos_alunos = string_todos_alunos + "E-mail: " + str(dado["email"]) + '\n\n'
        
        sg.Popup('-------- LISTA DE ALUNOS ----------', string_todos_alunos)
    
    def seleciona_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR ALUNO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o nome do aluno:', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona amigo').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        self.close()
        return nome
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
    
    def mostra_mensagem(self, msg):
        sg.popup(" ",msg)