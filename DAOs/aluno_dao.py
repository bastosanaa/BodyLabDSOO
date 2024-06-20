from DAOs.dao import DAO
from entidade.aluno import Amigo

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add (self, aluno: Aluno):
