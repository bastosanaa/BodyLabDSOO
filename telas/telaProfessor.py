import PySimpleGUI as sg
from telas.telaAbstrata import TelaAbstrata
from Exception.NumeroTelefoneInvalidoException import NumeroInvalido
from Exception.NomeNaoEhAlfa import NomeNaoEhAlfa
from Exception.EmailInvalido import EmailInvalido
from Exception.SalarioInválido import SalarioInvalido
from Exception.CPFinvalido import CPFinvalido
from telas.telaAbstrata import TelaAbstrata

from modelos.turno import Turno

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
        "5" : 5,
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
            [sg.Radio('Relatorio Professores por Turno', "RD1", key='5')],
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

    def mostra_professor(self, dados_professores):

        sg.ChangeLookAndFeel('DarkPurple1')
        lista_professores = [[
                    dados["cpf"],
                    dados["nome"],
                    dados["numero_telefone"],
                    dados["email"],
                    dados["salario"],
                    dados["turno"]
                ] for dados in dados_professores]

        headers = ["CPF", "Nome", "Telefone", "E-mail", "Salário", "Turno"]

        layout = [
            [sg.Column([[sg.Text('Lista de Professores da BodyLab', justification='center', font=('Helvetica', 20, 'bold'))]],
                    expand_x=True)],
            [sg.Table(values=lista_professores, headings=headers, display_row_numbers=False, auto_size_columns=True,
                    font=('Helvetica', 12),
                    size=(70, 40), num_rows=min(25, len(lista_professores)), col_widths=[15, 20, 15, 20, 50])],
            [sg.Button('OK', button_color=('white', 'green'))]
        ]


        self.__window = sg.Window('Sistema BodyLab').Layout(layout)

        button, values = self.open()
        self.close()

    def pega_dados_alterar_professor(self):
        sg.ChangeLookAndFeel('DarkPurple1')

        layout = [
        [sg.Text("insira os dados do professor a ser removido", font=('Helvetica', 25, 'bold'), justification='center')],
        [sg.Text('CPF: ', )],
        [sg.InputText('', key='cpf')],
        [sg.Button('Confirmar', button_color=('white', 'green')), sg.Button('Cancelar', button_color=('white', 'red'))]
        ]

        self.__window = sg.Window('Sistema BodyLab').Layout(layout)

        button, values = self.open()
        self.close()

        if button == 'Confirmar':
            cpf = values['cpf']
            cpf = ''.join(filter(str.isdigit, cpf))

            try:
                self.verifica_cpf(cpf)
            except CPFinvalido:
                self.mostra_mensagem("Tente Novamente. CPF inválido.")
            except ValueError:
                self.mostra_mensagem("Tente Novamente. Preencha todos os campos")
                return


            return  cpf
                

    def pega_alteracoes_professor(self, dados_professor):
        sg.ChangeLookAndFeel('DarkPurple1')

        turnos = ["matutino", "vespertino", "noturno"]

        layout = [
        [sg.Text('Alterar Professor', font=('Helvetica', 25, 'bold'), justification='center')],
        [sg.Text('Dados do professor:', font=('Helvetica', 15, 'bold'), justification='center')],
        [sg.Text(f"Nome: {dados_professor['nome']}")],
        [sg.Text(f"Número de Telefone: {dados_professor['numero_telefone']}")],
        [sg.Text(f"E-mail: {dados_professor['email']}")],
        [sg.Text(f"Turno: {dados_professor['turno']}")],
        [sg.Text(f"Salário: {dados_professor['salario']}")],
        [sg.Text('Alterações:', font=('Helvetica', 15, 'bold'), justification='center')],
        [sg.Text('Nome: ', )],
        [sg.InputText('', key='nome')],
        [sg.Text('Número de Telefone: (apenas números)')],
        [sg.InputText('', key='numero_telefone')],
        [sg.Text('E-mail: ')],
        [sg.InputText('', key='email')],
        [sg.Text('Turno: ')],
        [sg.Combo(turnos, key='turno', readonly=True)],
        [sg.Text('Salário: (apenas números)')],
        [sg.InputText('', key='salario')],
        [sg.Button('Confirmar', button_color=('white', 'green')), sg.Button('Cancelar', button_color=('white', 'red'))]
        ]

        self.__window = sg.Window('Sistema BodyLab').Layout(layout)

        button, values = self.open()
        self.close()

        if button == 'Confirmar':
            nome = values['nome']
            numero_telefone = values['numero_telefone']
            email = values['email']
            turno = values['turno']
            salario = values['salario']
            print(salario)

            try:
                self.verifica_nome(nome)
                self.verifica_telefone(numero_telefone)
                self.verifica_email(email)
                self.verifica_turno(turno)
                self.verifica_salario(salario)
            except NomeNaoEhAlfa:
                self.mostra_mensagem("Tente Novamente. Nome inválido")
                return
            except NumeroInvalido:
                self.mostra_mensagem("Tente Novamente. Número de telefone inválido (utilize apenas números)")
                return
            except EmailInvalido:
                self.mostra_mensagem("Tente Novamente. Email inválido")
                return
            except SalarioInvalido:
                self.mostra_mensagem("Tente Novamente. Salário inválido (dê um salário digno ao seu funcionário!)")
                return
            except ValueError:
                self.mostra_mensagem("Tente Novamente. Preencha todos os campos")
                return

            return {
                "nome": nome,
                "numero_telefone": numero_telefone,
                "email": email,
                "turno": turno,
                "salario": salario
            }
            


    def pega_dados_novo_professor(self):
        sg.ChangeLookAndFeel('DarkPurple1')

        turnos = ["matutino", "vespertino", "noturno"]

        layout = [
            [sg.Text("Cadastrar Professor", font=('Helvetica', 25, 'bold'), justification='center')],
            [sg.Text('Nome: ', )],
            [sg.InputText('', key='nome')],
            [sg.Text('CPF: ', )],
            [sg.InputText('', key='cpf')],
            [sg.Text('Número de Telefone: (apenas números)')],
            [sg.InputText('', key='numero_telefone')],
            [sg.Text('E-mail: ')],
            [sg.InputText('', key='email')],
            [sg.Text('Turno: ')],
            [sg.Combo(turnos, key='turno', readonly=True)],
            [sg.Text('Salário: (apenas números)')],
            [sg.InputText('', key='salario')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Button('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistema BodyLab', layout)

        button, values = self.open()
        self.close()

        if button == 'Confirmar':
            nome = values['nome']
            cpf = values['cpf']
            numero_telefone = values['numero_telefone']
            email = values['email']
            turno = values['turno']
            salario = values['salario']

            cpf = ''.join(filter(str.isdigit, cpf))

            # Realizando as verificações
            try:
                self.verifica_nome(nome)
                self.verifica_cpf(cpf)
                self.verifica_telefone(numero_telefone)
                self.verifica_email(email)
                self.verifica_turno(turno)
                self.verifica_salario(salario)
            except NomeNaoEhAlfa:
                self.mostra_mensagem("Tente Novamente. Nome inválido")
                return
            except NumeroInvalido:
                self.mostra_mensagem("Tente Novamente. Número de telefone inválido (utilize apenas números)")
                return
            except EmailInvalido:
                self.mostra_mensagem("Tente Novamente. Email inválido")
                return
            except SalarioInvalido:
                self.mostra_mensagem("Tente Novamente. Salário inválido (dê um salário digno ao seu funcionário!)")
                return
            except CPFinvalido:
                self.mostra_mensagem("Tente Novamente. CPF inválido.")
            except ValueError:
                self.mostra_mensagem("Tente Novamente. Preencha todos os campos")
                return

            return {
                "nome": nome,
                "cpf": cpf,
                "numero_telefone": numero_telefone,
                "email": email,
                "turno": turno,
                "salario": salario
            }
    
    def pega_dados_remover_professor(self):
        sg.ChangeLookAndFeel('DarkPurple1')

        layout = [
        [sg.Text("insira o cpf do professor a ser removido", font=('Helvetica', 25, 'bold'), justification='center')],
        [sg.Text('Cpf: ', )],
        [sg.InputText('', key='cpf')],
        [sg.Button('Confirmar', button_color=('white', 'green')), sg.Button('Cancelar', button_color=('white', 'red'))]
        ]

        self.__window = sg.Window('Sistema BodyLab', layout)

        button, values = self.open()
        self.close()

        if button == 'Confirmar':
            cpf = values['cpf']
            cpf = ''.join(filter(str.isdigit, cpf))

            return cpf
                

    def mostrar_relatorio_prof_turno(self, professores_por_turno):
        sg.ChangeLookAndFeel('DarkPurple1')

        layout = [
        [sg.Text("Professores por turno", font=('Helvetica', 25, 'bold'), justification='center')],
        [sg.Text(f"Matutino: {professores_por_turno['matutino']} professor(es)")],
        [sg.Text(f"Vespertino: {professores_por_turno['vespertino']} professor(es)")],
        [sg.Text(f"Noturno: {professores_por_turno['noturno']} professor(es)")],
        [sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]

        self.__window = sg.Window('Sistema BodyLab').Layout(layout)


        while True:
            event, values = self.__window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break

        self.__window.close()

    # verificacoes de entrada na criacao do professor
    
    def verifica_nome(self, nome):
        
            if nome:
                nome = nome.replace(' ', '')
                if not nome.isalpha():
                    raise NomeNaoEhAlfa
                return
            raise ValueError
        # except ValueError:
        #     self.mostra_mensagem("Tente Novamente. O campo nome não foi preenchido corretamente")
    
    def verifica_telefone(self, numero_telefone):
            if numero_telefone:
                if len(numero_telefone) < 9 or len(numero_telefone) > 12:
                    raise NumeroInvalido
                numero_telefone = int(numero_telefone)
                return
            raise ValueError

    def verifica_email(self, email):
            if email:
                if '@' not in email:
                    raise EmailInvalido
                return
            raise ValueError
    
    def verifica_turno(self, turno):
            if turno:
                return
            raise ValueError
        
    def verifica_salario(self, salario):
        salario_minimo = 1420
        if salario:
            salario = int(salario)
            if salario < salario_minimo:
                raise SalarioInvalido
            return
        raise ValueError
    
    def verifica_cpf(self,cpf) -> bool:
        if cpf:
            cpf = ''.join(filter(str.isdigit, cpf))
            
            if len(cpf) != 11:
                raise CPFinvalido

            if cpf == cpf[0] * len(cpf):
                raise CPFinvalido

            soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
            primeiro_digito_verificador = (soma * 10 % 11) % 10

            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            segundo_digito_verificador = (soma * 10 % 11) % 10

            if cpf[-2] == str(primeiro_digito_verificador) and cpf[-1] == str(segundo_digito_verificador):
                return
            raise CPFinvalido
        raise ValueError
        

    
