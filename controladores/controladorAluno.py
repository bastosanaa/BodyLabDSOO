from Exception.AlunoDuplicado import AlunoDuplicado
from Exception.NumeroTelefoneInvalidoException import NumeroTelefoneInvalido
from Exception.NomeNaoEhAlfa import NomeNaoEhAlfa
from Exception.EmailInvalido import EmailInvalido
from Exception.CepNaoEhNumero import CepNaoEhNumero
from telas.telaAluno import TelaAluno
from modelos.aluno import Aluno
from modelos.endereco import Endereco


class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema
        self.__alunos = []
        self.__matricula = None


    def cadastrar_aluno(self):
        try:
            dados_aluno = self.__tela_aluno.pega_dados_aluno()
            nome = dados_aluno['nome']
            if not nome.isalpha():
                raise NomeNaoEhAlfa()
            nome_aluno = self.buscar_aluno_por_nome(nome)
            if nome_aluno:
               raise AlunoDuplicado()
            if len(dados_aluno['numero_telefone']) != 11 or not dados_aluno['numero_telefone'].isnumeric:
               raise NumeroTelefoneInvalido()
            if '@' not in dados_aluno['email']:
                raise EmailInvalido()
            endereco = Endereco(dados_aluno['rua'], dados_aluno['complemento'], dados_aluno['bairro'], dados_aluno['cidade'], dados_aluno['cep'])
            if not endereco.cep.isnumeric():
                raise CepNaoEhNumero
            aluno = Aluno(dados_aluno['nome'], dados_aluno['numero_telefone'], dados_aluno['email'], matricula = None, endereco = endereco)
            self.__alunos.append(aluno)
            self.__tela_aluno.mostra_mensagem("Aluno cadastrado com sucesso")
            return aluno
        except NomeNaoEhAlfa as e:
            self.__tela_aluno.mostra_mensagem(str(e))
        except NumeroTelefoneInvalido as e:
            self.__tela_aluno.mostra_mensagem(str(e))
        except EmailInvalido as e:
            self.__tela_aluno.mostra_mensagem(str(e))
        except AlunoDuplicado as e:
            self.__tela_aluno.mostra_mensagem(str(e))
        except CepNaoEhNumero as e:
            self.__tela_aluno.mostra_mensagem(str(e))

    def aluno_esta_cadastrado(self, nome_aluno):
        for aluno in self.__alunos:
            if aluno.nome == nome_aluno:
                return True
        return False

    def remover_aluno(self):
        nome = self.__tela_aluno.seleciona_aluno()
        aluno = self.buscar_aluno_por_nome(nome)
        if not aluno:
            self.__tela_aluno.mostra_mensagem("Aluno não encontrado")
        else:
            self.__alunos.remove(aluno)
            self.__tela_aluno.mostra_mensagem("Aluno removido com sucesso")

    def buscar_aluno_por_nome(self, nome_aluno):
        for aluno in self.__alunos:
            if aluno.nome == nome_aluno:
                return aluno
        return None

    def alterar_aluno(self):
        nome_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.buscar_aluno_por_nome(nome_aluno)
        if not aluno:
            self.__tela_aluno.mostra_mensagem("Aluno não encontrado")
        else:
            dados_aluno = self.__tela_aluno.pega_dados_alterar_aluno()
            if 'nome' in dados_aluno:
                if not dados_aluno['nome'].isalpha():
                    raise NomeNaoEhAlfa()
                aluno.nome = dados_aluno['nome']
            if 'numero_telefone' in dados_aluno:
                if len(dados_aluno['numero_telefone']) != 11 or not dados_aluno['numero_telefone'].isnumeric:
                    raise NumeroTelefoneInvalido()
                aluno.numero_telefone = dados_aluno['numero_telefone']
            if 'email' in dados_aluno:
                if '@' not in dados_aluno['email']:
                    raise EmailInvalido()
                aluno.email = dados_aluno['email']
            if 'endereco' in dados_aluno:
                aluno.endereco = dados_aluno['endereco']
            self.__tela_aluno.mostra_mensagem("Aluno alterado com sucesso")

    def listar_alunos(self):
        if not self.__alunos:
            self.__tela_aluno.mostra_mensagem("Nenhum aluno cadastrado")
        else:
            for aluno in self.__alunos:
                dados_aluno = {
                    'nome': aluno.nome,
                    'numero_telefone': aluno.numero_telefone,
                    'email': aluno.email,
                    'endereco': aluno.endereco
                }
                self.__tela_aluno.mostra_aluno(dados_aluno)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_aluno, 2: self.remover_aluno, 3: self.listar_alunos, 4: self.alterar_aluno, 0: self.retornar}

        while True:
            try:
                opcao_escolhida = self.__tela_aluno.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            except NumeroTelefoneInvalido:
                self.__tela_aluno.mostra_mensagem("Número de telefone inválido")

    def retornar(self):
        self.__controlador_sistema.abre_tela()