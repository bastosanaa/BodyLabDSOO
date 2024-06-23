from DAOs.dao import DAO
from modelos.aluno import Aluno

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        if aluno is not None and isinstance(aluno, Aluno) and isinstance(aluno.cpf, str):
            super().add(aluno.cpf, aluno)

    def get(self, cpf: str):
        if isinstance(cpf, str):
            return super().get(cpf)

    def remove(self, cpf: str):
        if isinstance(cpf, str):
            super().remove(cpf)
            self.__dump()

    def get_all(self):
        return super().get_all()

    def update(self, aluno: Aluno):
        if aluno is not None and isinstance(aluno, Aluno) and isinstance(aluno.cpf, str):
            super().update(aluno.cpf, aluno)
