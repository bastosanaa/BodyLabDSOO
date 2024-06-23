import PySimpleGUI as sg
from modelos.endereco import Endereco
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
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, "Cancelar"):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("Aluno", font=('Helvetica', 25, 'bold'))],
            [sg.Radio('Cadastrar Aluno', "RD1", key='1')],
            [sg.Radio('Remover Aluno', "RD1", key='2')],
            [sg.Radio('Listar Alunos', "RD1", key='3')],
            [sg.Radio('Alterar Dado do Aluno', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar',button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistma BodyLab').Layout(layout)

    def pega_dados_aluno(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("Cadastrar Aluno", font=('Helvetica', 25, 'bold'), justification='center')],
            [sg.Text("CPF: ")],
            [sg.InputText('', key='cpf')],
            [sg.Text('Nome: ', )],
            [sg.InputText('', key='nome')],
            [sg.Text('Numero de Telefone: ')],
            [sg.InputText('', key='numero_telefone')],
            [sg.Text('E-mail: ')],
            [sg.InputText('', key='email')],
            [sg.Text('Rua: ')],
            [sg.InputText('', key='rua')],
            [sg.Text('Complemento: ')],
            [sg.InputText('', key='complemento')],
            [sg.Text('Bairro: ')],
            [sg.InputText('', key='bairro')],
            [sg.Text('Cidade: ')],
            [sg.InputText('', key='cidade')],
            [sg.Text('CEP: ')],
            [sg.InputText('', key='cep')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistema BodyLab').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        rua = values['rua']
        complemento = values['complemento']
        bairro = values['bairro']
        cidade = values['cidade']
        cep = values['cep']
        nome = values['nome']
        numero_telefone = values['numero_telefone']
        email = values['email']

        self.close()
        return {"cpf": cpf, "nome": nome, "numero_telefone": numero_telefone, "email": email,
                "rua": rua, "complemento": complemento, "bairro": bairro, "cidade": cidade, "cep": cep}

    def pega_dados_alterar_aluno(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("Alterar Dados do Aluno", font=('Helvetica', 20, 'bold'), justification='center')],
            [sg.Text('Nome: ')],
            [sg.InputText('', key='nome')],
            [sg.Text('Numero de Telefone: ')],
            [sg.InputText('', key='numero_telefone')],
            [sg.Text('E-mail: ')],
            [sg.InputText('', key='email')],
            [sg.Text('Rua: ')],
            [sg.InputText('', key='rua')],
            [sg.Text('Complemento: ')],
            [sg.InputText('', key='complemento')],
            [sg.Text('Bairro: ')],
            [sg.InputText('', key='bairro')],
            [sg.Text('Cidade: ')],
            [sg.InputText('', key='cidade')],
            [sg.Text('CEP: ')],
            [sg.InputText('', key='cep')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistema BodyLab').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        numero_telefone = values['numero_telefone']
        email = values['email']
        endereco = Endereco(values['rua'], values['complemento'], values['bairro'], values['cidade'], values['cep'])

        self.close()
        return {"nome": nome, "numero_telefone": numero_telefone, "email": email, "endereco": endereco},

    def lista_de_alunos(self, dados_alunos):
        lista_alunos = [[
            dados["cpf"],
            dados["nome"],
            dados["numero_telefone"],
            dados["email"],
            f"{dados['endereco'].rua}, {dados['endereco'].complemento}, {dados['endereco'].bairro}, {dados['endereco'].cidade}, {dados['endereco'].cep}"
        ] for dados in dados_alunos]

        headers = ["CPF", "Nome", "Telefone", "E-mail", "Endereço"]

        layout = [
            [sg.Column([[sg.Text('Lista de Alunos da BodyLab', justification='center', font=('Helvetica', 20, 'bold'))]],
                       expand_x=True)],
            [sg.Table(values=lista_alunos, headings=headers, display_row_numbers=False, auto_size_columns=True,
                      font=('Helvetica', 12),
                      size=(70, 40), num_rows=min(25, len(lista_alunos)), col_widths=[15, 20, 15, 20, 50])],
            [sg.Button('OK', button_color=('white', 'green'))]
        ]

        self.__window = sg.Window('Sistema BodyLab').Layout(layout)

        button, values = self.open()
        self.close()

    def seleciona_aluno(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text('seleciona aluno', font=("Helvica", 20, 'bold'))],
            [sg.Text('Digite o cpf do aluno:', font=("Helvica", 15))],
            [sg.Text('cpf:'), sg.InputText('', key='cpf')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistema BodyLab').Layout(layout)


        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, msg):
        layout = [
            [sg.Text(msg, font=('Helvetica', 15, 'bold'))],
            [sg.Button('OK')]
        ]

        self.__window = sg.Window('Mensagem', layout)

        while True:
            event, values = self.__window.read()
            if event in (sg.WINDOW_CLOSED, 'OK'):
                break

        self.__window.close()
