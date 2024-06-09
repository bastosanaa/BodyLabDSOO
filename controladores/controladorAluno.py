from telas.telaAluno import TelaAluno
from modelos.aluno import Aluno
class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema
        self.__alunos = []
        self.__matricula = None


    def cadastrar_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        nome = dados_aluno['nome']
        nome_aluno = self.buscar_aluno_por_nome(nome)
        if nome_aluno:
            self.__tela_aluno.mostra_mensagem("Aluno já cadastrado")
            return
        numero_telefone = dados_aluno['numero_telefone']
        email = dados_aluno['email']
        aluno = Aluno(nome, numero_telefone, email, matricula = None)
        self.__alunos.append(aluno)
        self.__tela_aluno.mostra_mensagem("Aluno cadastrado com sucesso")
        return aluno


    def remover_aluno(self):
        aluno = self.__tela_aluno.seleciona_aluno()
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)
            self.__tela_aluno.mostra_mensagem("Aluno removido com sucesso")

        else:
            self.__tela_aluno.mostra_mensagem("Aluno não encontrado")

    def buscar_aluno_por_nome(self, nome_aluno):
        for aluno in self.__alunos:
            if aluno.nome == nome_aluno:
                return aluno
        return None

    def listar_alunos(self):
        if not self.__alunos:
            self.__tela_aluno.mostra_mensagem("Nenhum aluno cadastrado")
        else:
            for aluno in self.__alunos:
                self.__tela_aluno.mostra_aluno(aluno)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_aluno, 2: self.remover_aluno, 3: self.listar_alunos, 4: self.buscar_aluno_por_nome, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_aluno.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abre_tela()