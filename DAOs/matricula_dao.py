from DAOs.dao import DAO
from modelos.matricula import Matricula

class MatriculaDAO(DAO):
    def __init__(self):
        super().__init__('matriculas.pkl')

    def add(self, matricula: Matricula):
        if matricula is not None and isinstance(matricula, Matricula):
            super().add(matricula.id_matricula, matricula)

    def get(self, id_matricula: str):
        if isinstance(id_matricula, str):
            return super().get(id_matricula)

    def remove(self, id_matricula: str):
        if isinstance(id_matricula, str):
            return super().remove(id_matricula)

    def get_all(self):
        return super().get_all()