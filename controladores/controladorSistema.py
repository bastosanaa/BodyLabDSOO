from telas.telaSistema import TelaSistema
from controladores.controladorProfessor import ControladorProfessor

class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_professor = ControladorProfessor(self)

    @property
    def controlador_professor(self):
        return self.__controlador_professor
    
    def cadastra_professore(self):
        self.__controlador_professor.abre_tela()

    def cadastra_aluno(self):
        pass

    def cadastra_ficha(self):
        pass
    
    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_professore, 2: self.cadastra_aluno, 3: self.cadastra_ficha}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
    
