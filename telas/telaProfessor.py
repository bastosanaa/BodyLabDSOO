from telas.telaAbstrata import TelaAbstrata
import PySimpleGUI as sg
from modelos.endereco import Endereco
from telas.telaAbstrata import TelaAbstrata

class TelaProfessor(TelaAbstrata):


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

        print(values)
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

    def pega_dados_professor(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("Cadastrar Professor", font=('Helvetica', 25, 'bold'), justification='center')],
            [sg.Text('Nome: ', )],
            [sg.InputText('', key='nome')],
            [sg.Text('Numero de Telefone: ')],
            [sg.InputText('', key='numero_telefone')],
            [sg.Text('E-mail: ')],
            [sg.InputText('', key='email')],
            [sg.Text('Turno: ')],
            [sg.InputText('', key='turno')],
            [sg.Text('Salario: ')],
            [sg.InputText('', key='salario')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistema BodyLab').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        numero_telefone = values['numero_telefone']
        email = values['email']
        rua = values['rua']
        complemento = values['complemento']
        bairro = values['bairro']
        cidade = values['cidade']
        cep = values['cep']

        self.close()
        return {"nome": nome, "numero_telefone": numero_telefone, "email": email, "rua": rua,
                "complemento": complemento, "bairro": bairro, "cidade": cidade, "cep": cep}