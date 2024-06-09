from abc import ABC, abstractmethod
from modelos.turno import Turno

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, numero_telefone: int, email: str):
        if isinstance(nome, str):
            self.__nome = nome
        self.__numero_telefone = numero_telefone
        if isinstance(email, str):
            self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def numero_telefone(self):
        return self.__numero_telefone

    @numero_telefone.setter
    def numero_telefone(self, numero_telefone):
        if isinstance(numero_telefone, int):
            self.__numero_telefone = numero_telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if isinstance(email, str):
            self.__email = email

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
            self.__turno = turno
