from controladores.controladorSistema import ControladorSistema
from controladores.controladorMatricula import ControladorMatricula
from telas.telaAluno import TelaAluno
from modelos.aluno import Aluno

class ControladorAluno:
    def __init__(self):
        self.__controlador_sistema = ControladorSistema()
        self.__controlador_matricula = ControladorMatricula()
        self.__tela_aluno = TelaAluno()
        self.__alunos = []
