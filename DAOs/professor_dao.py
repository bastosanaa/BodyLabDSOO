from DAOs.dao import DAO
from modelos.professor import Professor

class ProfessorDAO(DAO):
    def __init__(self):
        super().__init__('professors.pkl')

    def add(self, professor: Professor):
        if professor is not None and isinstance(professor, Professor) and isinstance(professor.cpf, str):
            super().add(professor.cpf, professor)

    def get(self, cpf: str):
        if isinstance(cpf, str):
            return super().get(cpf)

    def remove(self, cpf: str):
        if isinstance(cpf, str):
            super().remove(cpf)

    def update(self, professor: Professor):
        if professor is not None and isinstance(professor, Professor) and isinstance(professor.cpf, str):
            super().update(professor.cpf, professor)

    def get_all(self):
        return super().get_all()