from DAOs.aluno_dao import AlunoDAO
from Exception.AlunoDuplicado import AlunoDuplicado
from Exception.NumeroTelefoneInvalidoException import NumeroInvalido
from Exception.NomeNaoEhAlfa import NomeNaoEhAlfa
from Exception.EmailInvalido import EmailInvalido
from Exception.CepNaoEhNumero import CepNaoEhNumero
from Exception.OpcaoInvalida import OpcaoInvalida
from telas.telaAluno import TelaAluno
from modelos.aluno import Aluno
from modelos.endereco import Endereco


class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema
        self.__alunos_dao = AlunoDAO()
        self.__matricula = None

    def cadastrar_aluno(self):
        try:
            dados_aluno = self.__tela_aluno.pega_dados_aluno()
            if dados_aluno is None:
                return
            cpf = dados_aluno['cpf']
            if not cpf.isnumeric() or len(cpf) != 11:
                raise NumeroInvalido()
            nome = dados_aluno['nome']
            if not nome.isalpha():
                raise NomeNaoEhAlfa()
            aluno_cpf = self.buscar_aluno_por_cpf(cpf)
            if aluno_cpf:
               raise AlunoDuplicado()
            if len(dados_aluno['numero_telefone']) != 11 or not dados_aluno['numero_telefone'].isnumeric:
               raise NumeroInvalido()
            if '@' not in dados_aluno['email']:
                raise EmailInvalido()
            endereco = Endereco(dados_aluno['rua'], dados_aluno['complemento'], dados_aluno['bairro'],
                                dados_aluno['cidade'], dados_aluno['cep'])
            if not endereco.cep.isnumeric():
                raise CepNaoEhNumero
            aluno = Aluno(dados_aluno['cpf'], dados_aluno['nome'], dados_aluno['numero_telefone'],
                          dados_aluno['email'], matricula = None, endereco = endereco)
            self.__alunos_dao.add(aluno)
            self.__tela_aluno.mostra_mensagem("Aluno cadastrado com sucesso")
            return aluno
        except (NomeNaoEhAlfa, NumeroInvalido, EmailInvalido, AlunoDuplicado, CepNaoEhNumero) as e:
            self.__tela_aluno.mostra_mensagem(str(e))

    def aluno_esta_cadastrado(self, nome_aluno):
        for aluno in self.__alunos_dao.get_all():
            if aluno.nome == nome_aluno:
                return True
        return False

    def remover_aluno(self):
        try:
            cpf = self.__tela_aluno.seleciona_aluno()
        except ValueError:
            self.__tela_aluno.mostra_mensagem("CPF inválido. Por favor, insira um número válido.")
            return
        aluno = self.__alunos_dao.get(cpf)
        if not aluno:
            self.__tela_aluno.mostra_mensagem("Aluno não encontrado")
        else:
            self.__alunos_dao.remove(cpf)
            self.__tela_aluno.mostra_mensagem("Aluno removido com sucesso")
    def buscar_aluno_por_cpf(self, cpf_aluno):
       return self.__alunos_dao.get(cpf_aluno)

    def alterar_aluno(self):
        cpf_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.buscar_aluno_por_cpf(cpf_aluno)
        try:
            if not aluno:
                self.__tela_aluno.mostra_mensagem("Aluno não encontrado")
            else:
                dados_aluno = self.__tela_aluno.pega_dados_alterar_aluno()
                if 'nome' in dados_aluno and dados_aluno['nome']:
                    if not dados_aluno['nome'].isalpha():
                        raise NomeNaoEhAlfa()
                    aluno.nome = dados_aluno['nome']
                if 'numero_telefone' in dados_aluno and dados_aluno['numero_telefone']:
                    if len(dados_aluno['numero_telefone']) != 11 or not dados_aluno['numero_telefone'].isnumeric:
                        raise NumeroInvalido()
                    aluno.numero_telefone = dados_aluno['numero_telefone']
                if 'email' in dados_aluno and dados_aluno['email']:
                    if '@' not in dados_aluno['email']:
                        raise EmailInvalido()
                    aluno.email = dados_aluno['email']
                if 'endereco' in dados_aluno and dados_aluno['endereco']:
                    aluno.endereco = dados_aluno['endereco']
                self.__alunos_dao.update(aluno)
                self.__tela_aluno.mostra_mensagem("Aluno alterado com sucesso")
        except (NumeroInvalido, EmailInvalido, OpcaoInvalida) as e:
            self.__tela_aluno.mostra_mensagem(str(e))

    def listar_alunos(self):
        alunos = self.__alunos_dao.get_all()
        if not alunos:
            self.__tela_aluno.mostra_mensagem("Nenhum aluno cadastrado")
        else:
            dados_alunos = []
            for aluno in alunos:
                dados_aluno = {
                    'cpf': aluno.cpf,
                    'nome': aluno.nome,
                    'numero_telefone': aluno.numero_telefone,
                    'email': aluno.email,
                    'endereco': aluno.endereco
                }
                dados_alunos.append(dados_aluno)
            self.__tela_aluno.lista_de_alunos(dados_alunos)



    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_aluno, 2: self.remover_aluno, 3: self.listar_alunos, 4: self.alterar_aluno, 0: self.retornar}

        while True:
            try:
                opcao_escolhida = self.__tela_aluno.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            except NumeroInvalido:
                self.__tela_aluno.mostra_mensagem("Número de telefone inválido")

    def retornar(self):
        self.__controlador_sistema.abre_tela()