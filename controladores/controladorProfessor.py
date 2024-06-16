from telas.telaProfessor import TelaProfessor

class ControladorProfessor():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_professor = TelaProfessor()
        self.__professores = []
        
    def mostrar_professores_cadastrados(self):
        pass

    def cadastar_professor(self):
        dados_professor = self.__tela_professor.pega_dados_professor()
        pass

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
            4: self.mostrar_professores_cadastrados,
            5: self.alterar_professor,
            6: self.relatorio_professores_turno,
            0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_professor.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()