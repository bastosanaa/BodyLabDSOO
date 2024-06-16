from telas.telaProfessor import TelaProfessor
from Exception.ProfessorDuplicado import ProfessorDuplicado
from modelos.professor import Professor

class ControladorProfessor():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_professor = TelaProfessor()
        self.__professores = []
        self.__professores_por_turno = {
            'matutino': 0,
            'vespertino': 0,
            'noturno': 0
        }

    @property
    def professores_por_turno(self):
        return self.__professores_por_turno
        
    def adicionar_professor_turno(self, turno):
        self.__professores_por_turno[turno] += 1

    def cadastar_professor(self):
        try:
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
                self.adicionar_professor_turno(turno)
                self.__tela_professor.mostra_mensagem("Professor adicionado com sucesso!")
            except ProfessorDuplicado:
                self.__tela_professor.mostra_mensagem("Erro. Este professor já está cadastrado no sistema.")
        except TypeError:
            self.__tela_professor.mostra_mensagem("Operação Cancelada.")

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
            self.__tela_professor.mostra_professor(dados_professor, contagem_professor, numero_professores)
        

    def selecionar_professor_a_alterar(self):
        #perguntar qual professor 
        if self.__professores:
            try:
                dados_professor = self.__tela_professor.pega_dados_alterar_professor()
                nome = dados_professor['nome']
                email = dados_professor['email']

                for professor in self.__professores:
                    if professor.nome == nome and professor.email == email:
                        dados_professor = {
                        'nome': professor.nome,
                        'numero_telefone' : professor.numero_telefone,
                        'email': professor.email,
                        'turno': professor.turno,
                        'salario': professor.salario
                        }
                        print(dados_professor)
                        self.alterar_professor_selecionado(professor,dados_professor)
                        return
            except TypeError as e:
                print(e)
                self.__tela_professor.mostra_mensagem("Operação Cancelada.")
        self.__tela_professor.mostra_mensagem("Nenhum professor cadastrado no sistema")

    def alterar_professor_selecionado(self, professor, dados_professor):
        #TERMINAR ESSA FUNCAO
        alteracoes = self.__tela_professor.pega_alteracoes_professor(dados_professor)
        print(professor)
        for key, value in alteracoes.items():
            if value:
                professor[key] = value
        print(professor)

    def remover_professor(self):
        if self.__professores:
            try:
                dados_professor = self.__tela_professor.pega_dados_remover_professor()
                nome = dados_professor['nome']
                email = dados_professor['email']

                for professor in self.__professores:
                    if professor.nome == nome and professor.email == email:
                        self.__professores.remove(professor)
                        self.__tela_professor.mostra_mensagem("Professor removido com sucesso!")
                        return
                self.__tela_professor.mostra_mensagem("Tente novamente. Professor não encontrado no sistema.")
                return
            except TypeError:
                self.__tela_professor.mostra_mensagem("Operação Cancelada.")
        self.__tela_professor.mostra_mensagem("Nenhum professor cadastrado no sistema")

    def relatorio_professores_turno(self):
        self.__tela_professor.mostrar_relatorio_prof_turno(self.__professores_por_turno)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastar_professor,
            2: self.remover_professor,
            3: self.selecionar_professor_a_alterar,
            4: self.listar_professores,
            5: self.relatorio_professores_turno,
            0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_professor.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()