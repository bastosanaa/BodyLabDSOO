from telas.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg
from Exception.NumeroTelefoneInvalidoException import NumeroTelefoneInvalido
from Exception.NomeNaoEhAlfa import NomeNaoEhAlfa
from Exception.EmailInvalido import EmailInvalido
from Exception.SalarioInválido import SalarioInvalido
from telas.telaAbstrata import TelaAbstrata

class TelaProfessor(TelaAbstrata):
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
        "4" : 4,
        "5" : 5
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
            [sg.Text("Professor", font=('Helvetica', 25))],
            [sg.Radio('Cadastrar Professor', "RD1", key='1')],
            [sg.Radio('Remover Professor', "RD1", key='2')],
            [sg.Radio('Alterar Professor Cadastrado', "RD1", key='3')],
            [sg.Radio('Listar Professores', "RD1", key='4')],
            [sg.Radio('Alterar Professor Cadastrado', "RD1", key='5')],
            [sg.Radio('Relatorio Professores por Turno', "RD1", key='6')],
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

    def pega_dados_novo_professor(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("Cadastrar Professor", font=('Helvetica', 25, 'bold'), justification='center')],
            [sg.Text('Nome: ', )],
            [sg.InputText('', key='nome')],
            [sg.Text('Número de Telefone: (apenas números)')],
            [sg.InputText('', key='numero_telefone')],
            [sg.Text('E-mail: ')],
            [sg.InputText('', key='email')],
            [sg.Text('Turno: ')],
            [sg.InputText('', key='turno')],
            [sg.Text('Salario: (apenas números)')],
            [sg.InputText('', key='salario')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistema BodyLab').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        numero_telefone = values['numero_telefone']
        email = values['email']
        turno = values['turno']
        salario = values['salario']
        self.close()

        self.verifica_nome(nome)
        self.verifica_telefone(numero_telefone)
        self.verifica_email(email)
        self.verifica_turno(turno)
        self.verifica_salario(salario)

        return {
                "nome": nome,
                "numero_telefone": numero_telefone,
                "email": email,
                "turno": turno,
                "salario": salario
                }
    
    # verificacoes de entrada na criacao do professor
    def verifica_nome(self, nome):
        try:
            if nome:
                if not nome.isalpha():
                    raise NomeNaoEhAlfa
                return
            raise ValueError
        except NomeNaoEhAlfa:
            self.mostra_mensagem("Tente Novamente. Nome inválido")
        except ValueError:
            self.mostra_mensagem("Tente Novamente. O campo nome não foi preenchido corretamente")
    
    def verifica_telefone(self, numero_telefone):
        try:
            if numero_telefone:
                if len(numero_telefone) < 9 or len(numero_telefone) > 12:
                    raise NumeroTelefoneInvalido
                numero_telefone = int(numero_telefone)
                return
            raise ValueError
        except NumeroTelefoneInvalido:

            self.mostra_mensagem("Tente Novamente. Número de telefone inválido (utilize apenas números)")
        except ValueError:

            self.mostra_mensagem("Tente Novamente. O campo número de telefone não foi preenchido corretamemte")

    def verifica_email(self, email):
        try:
            if email:
                if '@' not in email:
                    raise EmailInvalido
                return
            raise ValueError
        except EmailInvalido:

            self.mostra_mensagem("Tente Novamente. Email inválido")
        except ValueError:

            self.mostra_mensagem("Tente Novamente. O campo email não foi preenchido corretamente")
    
    def verifica_turno(self, turno):
        #verificar se turno pertence a classe turno
        try:
            if turno:
                return
            raise ValueError
        except ValueError:

            self.mostra_mensagem("Tente Novamente. O turno não foi preenchido corretamente")
        
    def verifica_salario(self, salario):
        salario_minimo = 1420
        try:
            if salario:
                salario = int(salario)
                if salario < salario_minimo:
                    raise SalarioInvalido
                return
            raise ValueError
        except SalarioInvalido:
            self.mostra_mensagem("Tente Novamente. Salário inválido (dê um salário digno ao seu funcionário!)")
        except ValueError:
            self.mostra_mensagem("Tente Novamente. O salário não foi preenchido corretamente")
