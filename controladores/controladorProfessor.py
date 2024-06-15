from telas.telaProfessor import TelaProfessor

class ControladorProfessor():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_professor = TelaProfessor()
        self.__professores = []
        
    def mostrar_professores_cadastrados(self):
        pass

    def cadastar_professor(self):
        pass

    def alterar_professor(self):
        pass

    def vizualizar_professor(self):
        pass

    def professores_por_turno(self):
        pass


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.mostrar_professores_cadastrados,
            2: self.cadastar_professor,
            3: self.vizualizar_professor,
            4: self.vizualizar_professor,
            5: self.professores_por_turno,
            0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_professor.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()