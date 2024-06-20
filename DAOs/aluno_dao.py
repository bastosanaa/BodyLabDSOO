from DAOs.dao import DAO
from modelos.aluno import Aluno

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        if aluno is not None and isinstance(aluno, Aluno):
            super().add(aluno.cpf, aluno)

    def get(self, cpf: str):
        if isinstance(cpf, str):
            return super().get(cpf)

    def remove(self, cpf: str):
        if isinstance(cpf, str):
            return super().remove(cpf)

    def get_all(self):
        return super().get_all()