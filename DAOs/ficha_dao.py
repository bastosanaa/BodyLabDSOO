from DAOs.dao import DAO
from modelos.ficha import Ficha

class FichaDAO(DAO):
    def __init__(self):
        super().__init__('fichas.pkl')

    def add(self, ficha: Ficha):
        if ficha is not None and isinstance(ficha, Ficha) and isinstance(ficha.id_ficha, int):
            super().add(ficha.id_ficha, ficha)

    def get(self, id_ficha: int):
        if isinstance(id_ficha, int):
            return super().get(id_ficha)

    def remove(self, id_ficha: int):
        if isinstance(id_ficha, int):
            super().remove(id_ficha)

    def update(self, ficha: Ficha):
        if ficha is not None and isinstance(ficha, Ficha) and isinstance(ficha.id_ficha, int):
            super().update(ficha.id_ficha, ficha)

    def get_all(self):
        return super().get_all()