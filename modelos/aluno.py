from modelos.turno import Turno
from modelos.pessoa import Pessoa
from modelos.matricula import Matricula
from modelos.endereco import  Endereco
from modelos.ficha import Ficha


class Aluno(Pessoa):
    def __init__(self, cpf: int , nome: str, numero_telefone: int,
                 email: str, matricula: Matricula, endereco: Endereco):
        super().__init__(cpf, nome, numero_telefone, email)
        if isinstance(matricula, Matricula):
            self.__matricula = matricula
        self.__ficha = ''
        self.__endereco = endereco
        self.__cpf = cpf


    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        if isinstance(endereco, Endereco):
            self.__endereco = endereco

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, Matricula):
            self.__matricula = matricula

    @property
    def ficha(self):
        return self.__ficha
