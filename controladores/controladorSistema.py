from telas.telaSistema import TelaSistema
from controladores.controladorProfessor import ControladorProfessor
from controladores.controladorAluno import ControladorAluno
from controladores.controladorMatricula import ControladorMatricula


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_professor = ControladorProfessor(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_matricula = ControladorMatricula(self)

    @property
    def controlador_professor(self):
        return self.__controlador_professor
    
    @property
    def controlador_aluno(self):
        return self.__controlador_aluno
    
    @property
    def controlador_matricula(self):
        return self.__controlador_matricula
    
    def cadastra_professor(self):
        self.__controlador_professor.abre_tela()
    
    def cadastra_matricula(self):
        self.__controlador_matricula.abre_tela()

    def cadastra_aluno(self):
        self.controlador_aluno.abre_tela()

    def cadastra_ficha(self):
        pass
    
    def inicializa_sistema(self):
        self.abre_tela()

    def retornar(self):
        exit()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_professor, 2: self.cadastra_aluno, 3: self.cadastra_matricula, 4: self.cadastra_ficha, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
    
