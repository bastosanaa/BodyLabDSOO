from modelos.plano import Plano
from modelos.turno import Turno
class Matricula():
    def __init__(self, id_matricula: int, turno: Turno, plano: Plano, mensalidade: float, aluno,
                 data_inicio_matricula, data_vencimento_matricula, data_termino_matricula) -> None:
        self.__data_inicio_matricula = data_inicio_matricula
        self.__data_vevncimento_matricula = data_vencimento_matricula
        self.__data_termino_matricula =  data_termino_matricula
        self.__id_matricula = id_matricula
        self.__plano = plano
        self.__turno = turno
        self.__mensalidade = mensalidade
        self.__aluno = aluno


    @property
    def id_matricula(self):
        return self.__id_matricula

    @id_matricula.setter
    def id_matricula(self, id_matricula):
        self.__id_matricula = id_matricula

    @property
    def plano(self):
        return self.__plano

    @plano.setter
    def plano(self, plano):
        if isinstance(plano, Plano):
            self.__plano = plano

    @property
    def mensalidade(self):
        return self.__mensalidade

    @mensalidade.setter
    def mensalidade(self, mensalidade):
        self.__mensalidade = mensalidade


    @property
    def aluno(self):
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno):
            self.__aluno = aluno

    @property
    def data_inicio_matricula(self):
        return self.__data_inicio_matricula

    @data_inicio_matricula.setter
    def data_inicio_matricula(self, data_inicio_matricula):
        self.__data_inicio_matricula = data_inicio_matricula

    @property
    def data_vencimento_matricula(self):
        return self.__data_vevncimento_matricula

    @data_vencimento_matricula.setter
    def data_vencimento_matricula(self, data_vencimento_matricula):
        self.__data_vevncimento_matricula = data_vencimento_matricula

    @property
    def data_termino_matricula(self):
        return self.__data_termino_matricula

    @data_termino_matricula.setter
    def data_termino_matricula(self, data_termino_matricula):
        self.__data_termino_matricula = data_termino_matricula

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        if isinstance(turno, Turno):
            self.__turno = turno