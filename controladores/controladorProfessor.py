from telas.telaProfessor import TelaProfessor
from Exception.ProfessorDuplicado import ProfessorDuplicado
from modelos.professor import Professor

class ControladorProfessor():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_professor = TelaProfessor()
        self.__professores = []
        
    def listar_professores(self):
        if not self.__professores:
            self.__tela_professor.mostra_mensagem("Nenhum professor cadastrado no sistema")
            return
        contagem_professor = 0
        numero_professores = len(self.__professores)
        for professor in self.__professores:
            contagem_professor += 1
            dados_professor = {
                'nome': professor.nome,
                'numero_telefone' : professor.numero_telefone,
                'email': professor.email,
                'turno': professor.turno,
                'salario': professor.salario
            }
            #arrumar uma tela bonitinha para mostrar os professores
            self.__tela_professor.mostra_professor(dados_professor, contagem_professor, numero_professores)
        

    def cadastar_professor(self):
        dados_professor = self.__tela_professor.pega_dados_novo_professor()
        nome = dados_professor['nome']
        numero_telefone = dados_professor['numero_telefone']
        email = dados_professor['email']
        turno = dados_professor['turno']
        salario = dados_professor['salario']

        try:
            for professor in self.__professores:
                if professor.nome == nome and professor.email == email:
                    raise ProfessorDuplicado
            novo_professor = Professor(nome, numero_telefone, email, turno, salario)
            self.__professores.append(novo_professor)
        except ProfessorDuplicado:
            self.__tela_professor.mostra_mensagem("Erro. Este professor já está cadastrado no sistema.")

    def alterar_professor(self):
        pass

    def vizualizar_professor(self):
        pass

    def professores_por_turno(self):
        pass

    def remover_professor(self):
        pass

    def relatorio_professores_turno(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastar_professor,
            2: self.remover_professor,
            3: self.alterar_professor,
            4: self.listar_professores,
            5: self.alterar_professor,
            6: self.relatorio_professores_turno,
            0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_professor.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()