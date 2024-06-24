from DAOs.dao import DAO
from modelos.ficha import Ficha

class fichaDAO(DAO):
    def __init__(self):
        super().__init__('fichas.pkl')

    def add(self, ficha: Ficha):
        if ficha is not None and isinstance(ficha, Ficha) and isinstance(ficha.cpf, str):
            super().add(ficha.cpf, ficha)

    def get(self, cpf: str):
        if isinstance(cpf, str):
            return super().get(cpf)

    def remove(self, cpf: str):
        if isinstance(cpf, str):
            super().remove(cpf)

    def update(self, ficha: Ficha):
        if ficha is not None and isinstance(ficha, Ficha) and isinstance(ficha.cpf, str):
            super().update(ficha.cpf, ficha)

    def get_all(self):
        return super().get_all()