from DAOs.dao import DAO
from modelos.matricula import Matricula

class MatriculaDAO(DAO):
    def __init__(self):
        super().__init__('matriculas.pkl')

    def add(self, matricula: Matricula):
        if matricula is not None and isinstance(matricula, Matricula) and isinstance(matricula.id_matricula, int):
            super().add(matricula.id_matricula, matricula)

    def get(self, id_matricula: int):
        if isinstance(id_matricula, int):
            return super().get(id_matricula)

    def remove(self, id_matricula: int):
        if isinstance(id_matricula, int):
            super().remove(id_matricula)
            self.__dump()

    def update(self, matricula: Matricula):
        if matricula is not None and isinstance(matricula, Matricula) and isinstance(matricula.id_matricula, int):
            super().update(matricula.id_matricula, matricula)

    def get_all(self):
        return super().get_all()