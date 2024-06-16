from modelos.pessoa import Pessoa
from modelos.turno import Turno


class Professor(Pessoa):
    def __init__(self, nome: str, numero_telefone: int, email: str, turno: str, salario: float):
        super().__init__(nome, numero_telefone, email)
        self.__salario = salario
        self.__turno = turno
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        if isinstance(salario, int):
            self.__salario = salario

    @property
    def turno(self):
        return self.__turno
    
    @turno.setter
    def turno(self, turno):
        if isinstance(turno, int):
            self.__salario = turno